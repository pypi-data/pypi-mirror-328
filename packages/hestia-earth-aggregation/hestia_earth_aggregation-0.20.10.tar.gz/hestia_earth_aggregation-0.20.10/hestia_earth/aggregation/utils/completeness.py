from functools import reduce
from hestia_earth.schema import SchemaType, TermTermType, CompletenessField, COMPLETENESS_MAPPING, CompletenessJSONLD


_DEFAULT_COMPLETENESS_MAPPING = {
    SchemaType.MANAGEMENT.value: {
        TermTermType.CROPRESIDUEMANAGEMENT.value: TermTermType.CROPRESIDUE.value
    }
}


def blank_node_completeness_key(blank_node: dict):
    term_type = blank_node.get('term', {}).get('termType')
    mapping = (
        COMPLETENESS_MAPPING.get(blank_node.get('@type')) or
        _DEFAULT_COMPLETENESS_MAPPING.get(blank_node.get('@type'))
    )
    return (mapping or {}).get(term_type)


IS_COMPLETE = {
    CompletenessField.ANIMALFEED.value: lambda product: product.get('termType') in [
        TermTermType.ANIMALPRODUCT.value,
        TermTermType.LIVEANIMAL.value,
        TermTermType.LIVEAQUATICSPECIES.value
    ]
}


def is_complete(node: dict, product: dict, blank_node: dict):
    completeness_key = blank_node_completeness_key(blank_node)
    return all([
        node.get('completeness', {}).get(completeness_key, False),
        IS_COMPLETE.get(completeness_key, lambda *args: True)(product)
    ]) if completeness_key else None


def group_completeness(completeness: dict, node: dict):
    for key in node.get('completeness', {}).keys():
        is_complete = node.get('completeness').get(key, False)
        completeness[key] = completeness.get(key, 0) + (1 if is_complete else 0)
    return completeness


def aggregate_completeness(values: list):
    def is_complete(key: str):
        return any([v.get('completeness', v).get(key) is True for v in values])

    completeness = CompletenessJSONLD().to_dict()
    keys = list(completeness.keys())
    keys.remove('@type')
    return completeness | reduce(lambda prev, curr: prev | {curr: is_complete(curr)}, keys, {})
