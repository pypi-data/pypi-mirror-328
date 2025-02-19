"""A GraphQL domain for Sphinx."""

from collections.abc import Iterable, Iterator, Sequence, Set
from typing import ClassVar, NamedTuple, Optional

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.states import Inliner
from graphql.language import ast as gql_ast
from graphql.language.parser import Parser
from graphql.language.token_kind import TokenKind
from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, Index, IndexEntry, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole
from sphinx.util.docfields import GroupedField, TypedField
from sphinx.util import logging
from sphinx.util.nodes import make_refnode
from sphinx.util.typing import OptionSpec, TextlikeNode

__version__ = "1.0.0"
LOGGER = logging.getLogger(__name__)
DEFAULT_SCHEMA_NAME = "__gqlschema__"


class ObjectEntry(NamedTuple):
    """Information about a declared object for use in indexing the domain.

    These are created in :method:`GQLObject.add_target_and_index`
    for use in :class:`GraphQLSchemaIndex`.
    """

    docname: str
    """The name of the Sphinx document that the object was declared in."""
    node_id: str
    """The identifier of the declared object.

    This is the fully qualified name of the type.
    They are already guaranteed to be unique
    or they would create conflicts in the schema.
    """


class OperationTypeField(TypedField):
    def make_field(
        self,
        types: dict[str, list[Node]],
        domain: str,
        items: tuple,  # type: ignore[type-arg]
        env: Optional[BuildEnvironment] = None,
        inliner: Optional[Inliner] = None,
        location: Optional[Element] = None,
    ) -> nodes.field:
        # Sphinx will allow the field to be parsed without a type.
        # That's not valid GraphQL, so use the default operation names
        # when the operation type is specified without a name.
        types.setdefault("query", [nodes.Text("Query")])
        types.setdefault("mutation", [nodes.Text("Mutation")])
        types.setdefault("subscription", [nodes.Text("Subscription")])
        valid_optypes = ("query", "mutation", "subscription")

        fieldname = nodes.field_name("", self.label)
        bodynode = self.list_type()
        for fieldarg, value in items:
            if value and value[0].rawsource:
                msg = (
                    f"optype field {fieldarg} has a description, which will be ignored"
                )
                LOGGER.warning(msg, type="graphqldomain", subtype="invalid_optype")

            par = nodes.paragraph()
            par += addnodes.literal_strong(fieldarg, fieldarg)
            if fieldarg not in valid_optypes:
                msg = (
                    f"Invalid operation type '{fieldarg}', "
                    f"should be one of: {', '.join(valid_optypes)}"
                )
                LOGGER.warning(msg, type="graphqldomain", subtype="invalid_optype")
            else:
                par += nodes.Text(": ")
                fieldtype = types[fieldarg]
                if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                    typename = fieldtype[0].astext()
                    par.extend(
                        self.make_xrefs(
                            self.typerolename,
                            domain,
                            typename,
                            addnodes.literal_emphasis,
                            env=env,
                            inliner=inliner,
                            location=location,
                        )
                    )
                else:
                    par += fieldtype

            bodynode += nodes.list_item("", par)

        fieldbody = nodes.field_body("", bodynode)
        return nodes.field("", fieldname, fieldbody)

    def make_xref(
        self,
        rolename: str,
        domain: str,
        target: str,
        innernode: type[TextlikeNode] = nodes.emphasis,
        contnode: Optional[Node] = None,
        env: Optional[BuildEnvironment] = None,
        inliner: Optional[Inliner] = None,
        location: Optional[Element] = None,
    ) -> Node:
        result = super().make_xref(
            rolename, domain, target, innernode, contnode, env, inliner, location
        )

        xref = None
        if isinstance(result, pending_xref):
            xref = result
        elif result.children and isinstance(result.children[0], pending_xref):
            xref = result.children[0]

        if xref and env:
            xref["gql:schema"] = env.ref_context.get("gql:schema")

        return result


def type_to_xref(
    target: str, env: BuildEnvironment, reftype: str = "any"
) -> pending_xref:
    """Create a pending_xref node, attaching schema context if applicable."""
    xref = pending_xref(
        "",
        nodes.Text(target),
        refdomain="gql",
        reftype=reftype,
        reftarget=target,
        refspecific=True,
    )
    xref["gql:schema"] = env.ref_context.get("gql:schema")
    return xref


class GQLObject(ObjectDescription[tuple[str, Optional[str]]]):
    """The base class for any GraphQL type."""

    option_spec: ClassVar[OptionSpec] = {
        "noindex": directives.flag,
    }

    obj_type: str
    """The name of the type.

    This is used as a key in the domain data and as the name of the Sphinx object type.
    Therefore any value of :attr:``obj_type`` must also exist in
    :attr:`GQLDomain.initial_data` and :attr:`GQLDomain.object_types`.
    """
    parent_type: Optional[str] = None

    def add_target_and_index(
        self, name: tuple[str, Optional[str]], sig: str, signode: desc_signature
    ) -> None:
        node_id = signode["fullname"]

        signode["ids"].append(node_id)
        if "noindex" not in self.options:
            self.env.domaindata["gql"][self.obj_type][signode["fullname"]] = (
                ObjectEntry(
                    self.env.docname,
                    node_id,
                )
            )

    def _handle_signature_directives(
        self, signode: desc_signature, ast_nodes: Sequence[gql_ast.ConstDirectiveNode]
    ) -> None:
        for directive_node in ast_nodes:
            signode += addnodes.desc_sig_space()

            signode += addnodes.desc_sig_operator("", "@")
            directive_name = directive_node.name.value
            signode += type_to_xref(directive_name, self.env, reftype="directive")

            self._handle_signature_const_arguments(signode, directive_node.arguments)

    def _handle_signature_const_arguments(
        self, signode: desc_signature, ast_nodes: Sequence[gql_ast.ConstArgumentNode]
    ) -> None:
        if not ast_nodes:
            return

        signode += addnodes.desc_sig_operator("", "(")

        for i, argument_node in enumerate(ast_nodes):
            if i != 0:
                signode += addnodes.desc_sig_punctuation("", ",")
                signode += addnodes.desc_sig_space()

            signode += addnodes.desc_sig_name("", argument_node.name.value)
            signode += addnodes.desc_sig_punctuation("", ":")
            signode += addnodes.desc_sig_space()
            self._handle_signature_literal(signode, argument_node.value)

        signode += addnodes.desc_sig_operator("", ")")

    def _handle_signature_input_values(
        self,
        signode: desc_signature,
        ast_nodes: Sequence[gql_ast.InputValueDefinitionNode],
    ) -> None:
        if not ast_nodes:
            return

        signode += addnodes.desc_sig_operator("", "(")

        for i, argument_node in enumerate(ast_nodes):
            if i != 0:
                signode += addnodes.desc_sig_punctuation("", ",")
                signode += addnodes.desc_sig_space()

            signode += addnodes.desc_sig_name("", argument_node.name.value)
            signode += addnodes.desc_sig_punctuation("", ":")
            signode += addnodes.desc_sig_space()
            self._handle_signature_type_reference(signode, argument_node.type)
            self._handle_signature_default_value(signode, argument_node.default_value)
            self._handle_signature_directives(signode, argument_node.directives)

        signode += addnodes.desc_sig_operator("", ")")

    def _handle_signature_default_value(
        self, signode: desc_signature, ast_nodes: Optional[gql_ast.ConstValueNode]
    ) -> None:
        if not ast_nodes:
            return

        signode += addnodes.desc_sig_space()
        signode += addnodes.desc_sig_operator("", "=")
        signode += addnodes.desc_sig_space()

        self._handle_signature_literal(signode, ast_nodes)

    def _handle_signature_literal(
        self, signode: desc_signature, ast_nodes: Optional[gql_ast.ConstValueNode]
    ) -> None:
        if isinstance(ast_nodes, gql_ast.ListValueNode):
            signode += addnodes.desc_sig_operator("", "[")
            for i, item_node in enumerate(ast_nodes.values):
                if i != 0:
                    signode += addnodes.desc_sig_punctuation("", ",")
                    signode += addnodes.desc_sig_space()

                self._handle_signature_literal(signode, item_node)

            signode += addnodes.desc_sig_operator("", "]")

        elif isinstance(ast_nodes, gql_ast.ObjectValueNode):
            signode += addnodes.desc_sig_operator("", "{")
            for i, field_node in enumerate(ast_nodes.fields):
                if i != 0:
                    signode += addnodes.desc_sig_punctuation("", ",")
                    signode += addnodes.desc_sig_space()

                signode += addnodes.desc_sig_name("", field_node.name.value)
                signode += addnodes.desc_sig_punctuation("", ":")
                signode += addnodes.desc_sig_space()
                self._handle_signature_literal(signode, field_node.value)

            signode += addnodes.desc_sig_operator("", "}")

        elif isinstance(ast_nodes, (gql_ast.IntValueNode, gql_ast.FloatValueNode)):
            signode += addnodes.desc_sig_literal_number("", ast_nodes.value)
        elif isinstance(ast_nodes, gql_ast.StringValueNode):
            signode += addnodes.desc_sig_operator("", '"')
            signode += addnodes.desc_sig_literal_string("", ast_nodes.value)
            signode += addnodes.desc_sig_operator("", '"')
        elif isinstance(ast_nodes, gql_ast.BooleanValueNode):
            signode += addnodes.desc_sig_keyword("", str(ast_nodes.value).lower())
        elif isinstance(ast_nodes, gql_ast.NullValueNode):
            signode += addnodes.desc_sig_keyword("", "null")
        elif isinstance(ast_nodes, gql_ast.EnumValueNode):
            signode += addnodes.desc_sig_name("", ast_nodes.value)
        # Variable values are a valid literal but not in schemas
        else:
            raise TypeError(f"Unknown literal node type '{type(ast_nodes)}'")

    def _handle_signature_type_reference(
        self,
        signode: desc_signature,
        ast_node: gql_ast.TypeNode,
    ) -> None:
        if isinstance(ast_node, gql_ast.NamedTypeNode):
            type_name = ast_node.name.value
            signode += type_to_xref(type_name, self.env)
        elif isinstance(ast_node, gql_ast.NonNullTypeNode):
            self._handle_signature_type_reference(signode, ast_node.type)
            signode += addnodes.desc_sig_operator("", "!")
        elif isinstance(ast_node, gql_ast.ListTypeNode):
            signode += addnodes.desc_sig_operator("", "[")
            self._handle_signature_type_reference(signode, ast_node.type)
            signode += addnodes.desc_sig_operator("", "]")
        else:
            raise TypeError(f"Unknown type node '{type(ast_node)}")

    def _resolve_names(
        self, name: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        """Use the parenting of objects to resolve the fullname attribute.

        By default an object can only be parented to a schema.
        Objects that are parented to something other than a schema should
        inherit from :class:`GQLChildObject`.
        """
        parent_name = self.env.ref_context.get("gql:schema")
        if parent_name:
            fullname = f"{parent_name}.{name}"
        else:
            fullname = name
        signode["fullname"] = fullname
        return (fullname, parent_name)


class GQLParentObject(GQLObject):
    """A base class for any GraphQL types that can have child entities."""

    def before_content(self) -> None:
        """Set the domain context to be this object."""
        if self.names:
            fullname, _ = self.names[-1]
            # GraphQL entities can only have on level of nesting,
            # so we only need to set and unset the context
            # rather than needing to maintain a stack.
            self.env.ref_context[f"gql:{self.obj_type}"] = fullname

    def after_content(self) -> None:
        """Unset the domain context."""
        self.env.ref_context[f"gql:{self.obj_type}"] = None


class GQLChildObject(GQLObject):
    """A base class for any GraphQL types that only exists as the child of another type.

    This class uses the context set by the parent :class:`GQLParentObject`
    to correctly prefix the name of this entity with the parent
    and tell Sphinx to associate this child with the parent.
    """

    parent_type: str
    """The value of the :attr:`obj_type` attribute on the parent object."""

    def _resolve_names(
        self, name: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        parent_name = self.env.ref_context.get(f"gql:{self.parent_type}")
        if parent_name:
            fullname = f"{parent_name}.{name}"
        else:
            fullname = name
        signode["fullname"] = fullname
        return (fullname, parent_name)


class GQLField(GQLChildObject):
    """A base class for any field type.

    See Also:
        https://spec.graphql.org/June2018/#FieldDefinition
    """

    doc_field_types = [
        GroupedField(
            "argument",
            label="Arguments",
            names=("arg", "argument"),
        ),
    ]

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        parser = Parser(sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_field_definition()
        parser.expect_token(TokenKind.EOF)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_input_values(signode, node.arguments)

        signode += addnodes.desc_sig_operator("", ":")
        signode += addnodes.desc_sig_space()

        self._handle_signature_type_reference(signode, node.type)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLDirective(GQLObject):
    """Represents the definition of a GraphQL Directive.

    See also:
        https://spec.graphql.org/June2018/#sec-Type-System.Directives
    """

    obj_type = "directive"
    doc_field_types = [
        GroupedField(
            "argument",
            label="Arguments",
            names=("arg", "argument"),
        ),
    ]

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#sec-Type-System.Directives
        parser = Parser("directive " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_directive_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("directive"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)
        signode += addnodes.desc_sig_space()
        signode += addnodes.desc_sig_operator("", "@")

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_input_values(signode, node.arguments)

        signode += addnodes.desc_sig_space()
        signode += addnodes.desc_sig_keyword("", "on")
        signode += addnodes.desc_sig_space()

        for i, location in enumerate(node.locations):
            if i != 0:
                signode += addnodes.desc_sig_space()
                signode += addnodes.desc_sig_operator("", "|")
                signode += addnodes.desc_sig_space()

            signode += nodes.Text(location.value)

        return self._resolve_names(name, signode)


class GQLEnum(GQLParentObject):
    """Represents the definition of a GraphQL Enum.

    See also:
        https://spec.graphql.org/June2018/#sec-Enums
    """

    obj_type = "enum"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#sec-Interfaces
        parser = Parser("enum " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_enum_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("enum"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLEnumValue(GQLChildObject):
    """Represents the definition of a value on a GraphQL Enum.

    See also:
        https://spec.graphql.org/June2018/#sec-Enums
    """

    obj_type = "enum:value"
    parent_type = "enum"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#EnumValueDefinition
        parser = Parser(sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_enum_value_definition()
        parser.expect_token(TokenKind.EOF)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLInput(GQLParentObject):
    """Represents the definition of a GraphQL Input Object.

    See also:
        https://spec.graphql.org/June2018/#sec-Input-Objects
    """

    obj_type = "input"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#sec-Input-Objects
        parser = Parser("input " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_input_object_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("input"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLInputField(GQLChildObject):
    """Represents the definition of a field on a GraphQL Input Object.

    See also:
        https://spec.graphql.org/June2018/#sec-Input-Objects
    """

    obj_type = "input:field"
    parent_type = "input"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        parser = Parser(sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_input_value_def()
        parser.expect_token(TokenKind.EOF)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        signode += addnodes.desc_sig_operator("", ":")
        signode += addnodes.desc_sig_space()

        self._handle_signature_type_reference(signode, node.type)

        self._handle_signature_default_value(signode, node.default_value)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLInterface(GQLParentObject):
    """Represents the definition of a GraphQL Interface.

    See also:
        https://spec.graphql.org/June2018/#sec-Interfaces
    """

    obj_type = "interface"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#sec-Interfaces
        parser = Parser("interface " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_interface_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("interface"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLInterfaceField(GQLField):
    """Represents the definition of a field on a GraphQL Interface.

    See also:
        https://spec.graphql.org/June2018/#sec-Interfaces
    """

    obj_type = "interface:field"
    parent_type = "interface"


class GQLScalar(GQLObject):
    """Represents the definition of a GraphQL Scalar.

    See also:
        https://spec.graphql.org/June2018/#sec-Scalars
    """

    obj_type = "scalar"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        parser = Parser("scalar " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_scalar_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("scalar"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLSchema(GQLParentObject):
    """Represents the definition of a GraphQL Schema.

    See also:
        https://spec.graphql.org/June2018/#sec-Schema
    """

    obj_type = "schema"
    option_spec: ClassVar[OptionSpec] = {
        "noindex": directives.flag,
        "name": directives.unchanged,
    }
    required_arguments = 0
    optional_arguments = 1
    doc_field_types = [
        OperationTypeField(
            "operationtypes",
            label="Operation types",
            names=("optype",),
            typerolename="type",
            typenames=(),
        ),
    ]

    def get_signatures(self) -> list[str]:
        if self.arguments:
            return super().get_signatures()

        return [""]

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        prefix = [nodes.Text("schema"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        directives = sig
        if directives:
            parser = Parser(directives, no_location=True)
            parser.expect_token(TokenKind.SOF)
            directive_nodes = parser.parse_const_directives()
            parser.expect_token(TokenKind.EOF)

            self._handle_signature_directives(signode, directive_nodes)

        name = self.options.get("name", DEFAULT_SCHEMA_NAME)
        signode["fullname"] = name
        return (name, None)


class GQLType(GQLParentObject):
    """Represents the definition of a GraphQL Type Object.

    See also:
        https://spec.graphql.org/June2018/#sec-Objects
    """

    obj_type = "type"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        # https://spec.graphql.org/June2018/#sec-Objects
        parser = Parser("type " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_object_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("type"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        interfaces = node.interfaces
        if interfaces:
            signode += addnodes.desc_sig_space()
            signode += addnodes.desc_sig_keyword("", "implements")
            signode += addnodes.desc_sig_space()
            for i, interface in enumerate(interfaces):
                if i != 0:
                    signode += addnodes.desc_sig_space()
                    signode += addnodes.desc_sig_operator("", "&")
                    signode += addnodes.desc_sig_space()

                interface_type = interface.name.value
                signode += type_to_xref(interface_type, self.env, reftype="interface")

        self._handle_signature_directives(signode, node.directives)

        return self._resolve_names(name, signode)


class GQLTypeField(GQLField):
    """Represents the definition of a field on a GraphQL Type Object.

    See also:
        https://spec.graphql.org/June2018/#sec-Objects
    """

    obj_type = "type:field"
    parent_type = "type"


class GQLUnion(GQLObject):
    """Represents the definition of a GraphQL Union.

    See also:
        https://spec.graphql.org/June2018/#sec-Unions
    """

    obj_type = "union"

    def handle_signature(
        self, sig: str, signode: desc_signature
    ) -> tuple[str, Optional[str]]:
        parser = Parser("union " + sig, no_location=True)
        parser.expect_token(TokenKind.SOF)
        node = parser.parse_union_type_definition()
        parser.expect_token(TokenKind.EOF)

        prefix = [nodes.Text("union"), addnodes.desc_sig_space()]
        signode += addnodes.desc_annotation(str(prefix), "", *prefix)

        name = node.name.value
        signode += addnodes.desc_name(name, name)

        self._handle_signature_directives(signode, node.directives)

        member_nodes = node.types
        if member_nodes:
            for i, member_node in enumerate(member_nodes):
                if i == 0:
                    signode += addnodes.desc_sig_space()
                    signode += addnodes.desc_sig_operator("", "=")
                    signode += addnodes.desc_sig_space()
                else:
                    signode += addnodes.desc_sig_space()
                    signode += addnodes.desc_sig_operator("", "|")
                    signode += addnodes.desc_sig_space()

                member_type = member_node.name.value
                signode += type_to_xref(member_type, self.env)

        return self._resolve_names(name, signode)


class GraphQLSchemaIndex(Index):
    """The index generator for the GraphQL domain."""

    name = "index"
    localname = "GraphQL Object Index"
    shortname = "index"

    def _anchor(self, fullname: str) -> str:
        return fullname.lower().split("(", 1)[0]

    def generate(
        self, docnames: Optional[Iterable[str]] = None
    ) -> tuple[list[tuple[str, list[IndexEntry]]], bool]:
        content: dict[str, list[IndexEntry]] = {}

        for fullname, _, objtype, docname, node_id, __ in sorted(
            self.domain.get_objects()
        ):
            # Only index top level objects to eliminate name collisions
            if objtype in ("enumvalue", "field"):
                continue

            name = fullname
            subtype = 0  # Always zero because we don't index child types
            anchor = node_id
            extra = ""
            qualifier = ""
            descr = ""
            entry = IndexEntry(name, subtype, docname, anchor, extra, qualifier, descr)

            entries = content.setdefault(fullname[0].lower(), [])
            entries.append(entry)

        sorted_content = sorted(content.items())

        return (sorted_content, True)


class GQLXRefRole(XRefRole):
    def process_link(
        self,
        env: BuildEnvironment,
        refnode: Element,
        has_explicit_title: bool,
        title: str,
        target: str,
    ) -> tuple[str, str]:
        title, target = super().process_link(
            env, refnode, has_explicit_title, title, target
        )

        if not has_explicit_title and title.startswith(f"{DEFAULT_SCHEMA_NAME}."):
            title = title.split(".", 1)[-1]

        refnode["gql:schema"] = env.ref_context.get("gql:schema")
        return (title, target)


class GraphQLDomain(Domain):
    """The definition of the GraphQL Sphinx Domain."""

    name = "gql"
    label = "GraphQL"
    object_types: dict[str, ObjType] = {
        "directive": ObjType("directive", "directive"),
        "enum": ObjType("enum", "enum"),
        "enum:value": ObjType("enum-value", "enum"),
        "input": ObjType("input", "input"),
        "input:field": ObjType("input-field", "input"),
        "interface": ObjType("interface", "interface"),
        "interface:field": ObjType("interface-field", "interface"),
        "scalar": ObjType("scalar", "scalar"),
        "schema": ObjType("schema", "schema"),
        "type": ObjType("type", "type"),
        "type:field": ObjType("type-field", "type"),
        "union": ObjType("union", "union"),
    }

    directives: dict[str, type[Directive]] = {
        "directive": GQLDirective,
        "enum": GQLEnum,
        "enum:value": GQLEnumValue,
        "input": GQLInput,
        "input:field": GQLInputField,
        "interface": GQLInterface,
        "interface:field": GQLInterfaceField,
        "scalar": GQLScalar,
        "schema": GQLSchema,
        "type": GQLType,
        "type:field": GQLTypeField,
        "union": GQLUnion,
    }

    # mypy complains because many types are allowed other than XRefRole.
    # However this class isn't going to be used for subclassing
    # so violating variance rules is acceptable.
    roles: dict[str, XRefRole] = {  # type: ignore[assignment]
        "directive": GQLXRefRole(),
        "enum": GQLXRefRole(),
        "enum:value": GQLXRefRole(),
        "input": GQLXRefRole(),
        "input:field": GQLXRefRole(),
        "interface": GQLXRefRole(),
        "interface:field": GQLXRefRole(),
        "scalar": GQLXRefRole(),
        "schema": GQLXRefRole(),
        "type": GQLXRefRole(),
        "type:field": GQLXRefRole(),
        "union": GQLXRefRole(),
    }

    initial_data: dict[str, dict[str, ObjectEntry]] = {
        "directive": {},
        "enum": {},
        "enum:value": {},
        "input": {},
        "input:field": {},
        "interface": {},
        "interface:field": {},
        "scalar": {},
        "schema": {},
        "type": {},
        "type:field": {},
        "union": {},
    }

    indices = [GraphQLSchemaIndex]

    def clear_doc(self, docname: str) -> None:
        for object_type in self.object_types:
            type_data = self.data[object_type]
            for fullname, entry in list(type_data.items()):
                if entry.docname == docname:
                    del type_data[fullname]

    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Optional[Element]:
        patterns = [target]

        # If the xref was created in the context of the schema,
        # allow references to other names in the schema
        # without needing to specify the name of the schema.
        schema_name = node.get("gql:schema")
        if schema_name and not target.startswith(f"{schema_name}."):
            patterns.append(f"{schema_name}.{target}")

        # If the xref was created outside the context of the schema,
        # allow references to names in the schema with the default name
        # without needing to use the name of the schema.
        if not schema_name and not target.startswith(f"{DEFAULT_SCHEMA_NAME}."):
            patterns.append(f"{DEFAULT_SCHEMA_NAME}.{target}")

        for object_type in self.object_types:
            type_data = self.data[object_type]
            for fullname, entry in list(type_data.items()):
                if fullname in patterns:
                    return make_refnode(
                        builder,
                        fromdocname,
                        entry.docname,
                        entry.node_id,
                        [contnode],
                        fullname,
                    )

        return None

    def resolve_any_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> list[tuple[str, Element]]:
        """Resolve the pending_xref ``node`` with the given ``target``.

        The reference comes from an "any" or similar role,
        which means that Sphinx doesn't know the type.

        For now we don't resolve "any" xref nodes.
        """
        return []

    def get_objects(self) -> Iterator[tuple[str, str, str, str, str, int]]:
        for object_type in self.object_types:
            type_data = self.data[object_type]
            for fullname, entry in list(type_data.items()):
                yield (
                    fullname,
                    fullname,
                    object_type,
                    entry.docname,
                    # Names already abide by the rules of anchors
                    # (https://spec.graphql.org/June2018/#Name).
                    entry.node_id,
                    1,
                )

    def merge_domaindata(
        self, docnames: Set[str], otherdata: dict[str, dict[str, ObjectEntry]]
    ) -> None:
        """Merge the data from multiple workers when working in parallel."""
        for typ, type_data in self.data.items():
            other_type_data = otherdata[typ]
            for fullname, other_entry in other_type_data.items():
                if fullname in type_data and other_entry != type_data[fullname]:
                    entry = type_data[fullname]
                    other_docname = self.env.doc2path(other_entry[0])
                    this_docname = self.env.doc2path(entry[0])
                    LOGGER.warning(
                        f"Duplicate GraphQL {typ} type definition {fullname} "
                        f"in {other_docname}, "
                        f"other instance is in {this_docname}"
                    )
                else:
                    type_data[fullname] = other_entry


def setup(app: Sphinx) -> dict[str, bool]:
    """Prepare the extension."""
    app.add_domain(GraphQLDomain)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
