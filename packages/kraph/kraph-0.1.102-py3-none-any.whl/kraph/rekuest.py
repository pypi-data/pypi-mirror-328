
from rekuest_next.structures.default import (
    get_default_structure_registry,
    id_shrink,
)
from rekuest_next.widgets import SearchWidget
from rekuest_next.api.schema import PortScope
from kraph.api.schema import (
    Reagent,
    Ontology,
    aget_ontology,
    ProtocolStep,
    aget_reagent,
    Graph,
    aget_graph,
    SearchGraphsQuery,
    Expression,
    aget_expression,
    SearchExpressionsQuery,
    aget_protocol_step,
    SearchEntitiesQuery,
    SearchReagentsQuery,
    SearchProtocolStepsQuery,
    SearchOntologiesQuery
)

structure_reg = get_default_structure_registry()

structure_reg.register_as_structure(
    Ontology,
    identifier="@kraph/ontology",
    aexpand=aget_ontology,
    ashrink=id_shrink,
    scope=PortScope.GLOBAL,
    default_widget=SearchWidget(
        query=SearchOntologiesQuery.Meta.document, ward="kraph"
    ),
)
structure_reg.register_as_structure(
    Graph,
    identifier="@kraph/graph",
    aexpand=aget_graph,
    ashrink=id_shrink,
    scope=PortScope.GLOBAL,
    default_widget=SearchWidget(
        query=SearchGraphsQuery.Meta.document, ward="kraph"
    ),
)
structure_reg.register_as_structure(
    Reagent,
    identifier="@kraph/reagent",
    aexpand=aget_reagent,
    ashrink=id_shrink,
    scope=PortScope.GLOBAL,
    default_widget=SearchWidget(
        query=SearchReagentsQuery.Meta.document, ward="kraph"
    ),
)

structure_reg.register_as_structure(
    Expression,
    identifier="@kraph/expression",
    aexpand=aget_expression,
    ashrink=id_shrink,
    scope=PortScope.GLOBAL,
    default_widget=SearchWidget(
        query=SearchExpressionsQuery.Meta.document, ward="kraph"
    ),
)

structure_reg.register_as_structure(
    ProtocolStep,
    identifier="@kraph/protocolstep",
    aexpand=aget_protocol_step,
    ashrink=id_shrink,
    scope=PortScope.GLOBAL,
    default_widget=SearchWidget(
        query=SearchProtocolStepsQuery.Meta.document, ward="kraph"
    ),
)
