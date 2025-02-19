import os
import json
import pytest
from unittest.mock import Mock, patch

from tests.utils import (
    overwrite_expected,
    SOURCE, fixtures_path, fake_download, fake_grouped_cycles, start_year, end_year, fake_aggregated_version
)
from hestia_earth.aggregation.cycle.utils import (
    AGGREGATION_KEYS, _update_cycle, format_terms_results, aggregate_with_matrix
)
from hestia_earth.aggregation.utils.quality_score import calculate_score
from hestia_earth.aggregation.site.utils import aggregate_sites
from hestia_earth.aggregation.models.terms import aggregate, map_blank_nodes

class_path = 'hestia_earth.aggregation.models.terms'
fixtures_folder = os.path.join(fixtures_path, 'cycle', 'terms')

_files = [f for f in os.listdir(fixtures_folder) if os.path.isfile(os.path.join(fixtures_folder, f))]


@pytest.mark.parametrize('filename', _files)
@patch('hestia_earth.aggregation.cycle.utils._aggregated_version', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.site.utils._aggregated_version', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.site.utils._aggregated_node', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.cycle.utils._aggregated_node', side_effect=fake_aggregated_version)
@patch('hestia_earth.aggregation.cycle.practice.download_hestia', side_effect=fake_download)
@patch('hestia_earth.aggregation.utils.queries.download_hestia', side_effect=fake_download)
@patch(f"{class_path}.download_hestia", side_effect=fake_download)
@patch('hestia_earth.aggregation.site.management._current_date', return_value='2025-01-01')
@patch('hestia_earth.aggregation.utils.queries._current_date', return_value='2025-01-01')
@patch('hestia_earth.aggregation.cycle.utils._timestamp', return_value='')
def test_aggregate(
    mock_1: Mock,
    mock_2: Mock,
    mock_3: Mock,
    mock_4: Mock,
    mock_5: Mock,
    mock_6: Mock,
    mock_7: Mock,
    mock_8: Mock,
    mock_9: Mock,
    mock_10: Mock,
    filename: str
):
    filepath = os.path.join(fixtures_folder, filename)
    with open(filepath, encoding='utf-8') as f:
        expected = json.load(f)

    product_name = filename.replace('-aggregated.jsonld', '')
    cycles, product, functional_unit = fake_grouped_cycles(product_name)
    include_matrix = aggregate_with_matrix(product)
    cycles = aggregate_sites(cycles, start_year, end_year)
    cycles = map_blank_nodes(AGGREGATION_KEYS, cycles)
    results = aggregate(AGGREGATION_KEYS, cycles)
    results = list(map(format_terms_results, results))
    results = list(map(_update_cycle(None, start_year, end_year, SOURCE, functional_unit, include_matrix), results))
    results = list(map(calculate_score, results))
    results = results
    overwrite_expected(filepath, results)
    assert results == expected
