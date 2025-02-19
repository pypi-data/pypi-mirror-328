from hestia_earth.schema import SchemaType, PracticeStatsDefinition
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import linked_node

from hestia_earth.aggregation.utils import _aggregated_version


def _new_practice(data):
    node = {'@type': SchemaType.PRACTICE.value}
    term = data.get('term') if isinstance(data, dict) else download_hestia(data)
    node['term'] = linked_node(term)
    value = data.get('value')
    if value is not None:
        node['value'] = [round(value, 8)]
        node['statsDefinition'] = PracticeStatsDefinition.CYCLES.value
    return node


def organic_practice():
    node = {'@type': SchemaType.PRACTICE.value}
    node['term'] = linked_node(download_hestia('organic'))
    node['value'] = [100]
    node['statsDefinition'] = PracticeStatsDefinition.CYCLES.value
    return _aggregated_version(node)
