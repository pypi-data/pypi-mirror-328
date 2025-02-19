from hestia_earth.schema import MeasurementJSONLD, MeasurementStatsDefinition, MeasurementMethodClassification
from hestia_earth.utils.model import linked_node
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name

from hestia_earth.aggregation.utils import _set_dict_array, _set_dict_single
from hestia_earth.aggregation.utils.term import should_aggregate


def _new_measurement(data: dict):
    measurement = MeasurementJSONLD().to_dict()
    measurement['term'] = linked_node(data.get('term'))
    measurement['methodClassification'] = MeasurementMethodClassification.COUNTRY_LEVEL_STATISTICAL_DATA.value

    value = data.get('value')
    if value is not None:
        measurement['value'] = [value]
        measurement['statsDefinition'] = MeasurementStatsDefinition.SITES.value

    _set_dict_array(measurement, 'observations', data.get('observations'))
    _set_dict_array(measurement, 'min', data.get('min'))
    _set_dict_array(measurement, 'max', data.get('max'))
    _set_dict_array(measurement, 'sd', data.get('sd'), True)

    _set_dict_single(measurement, 'startDate', data.get('startDate'))
    _set_dict_single(measurement, 'endDate', data.get('endDate'))

    if data.get('depthUpper') is not None:
        measurement['depthUpper'] = int(data.get('depthUpper'))
    if data.get('depthLower') is not None:
        measurement['depthLower'] = int(data.get('depthLower'))

    return measurement


def should_aggregate_measurement(measurement: dict):
    term = measurement.get('term', {})
    lookup = download_lookup(f"{term.get('termType')}.csv")
    value = get_table_value(lookup, 'termid', term.get('@id'), column_name('arrayTreatmentLargerUnitOfTime'))
    # ignore any measurement with time-split data
    return not value and should_aggregate(term)
