import pytest
from unittest.mock import MagicMock, patch
import pandas as pd

from fedwrap.census_acs.acs import get_acs_data, measure_function_map


SENTINEL_DF = pd.DataFrame({"ucgid": ["geo1"], "value": [1.0]})


def test_known_measure_dispatches_correctly():
    with patch("fedwrap.census_acs.acs.get_total_pop", return_value=SENTINEL_DF) as mock_fn:
        result = get_acs_data("TOTAL_POP", "2022", "county")
        mock_fn.assert_called_once_with("2022", "county", False)
    assert result is SENTINEL_DF


def test_as_percent_forwarded():
    with patch("fedwrap.census_acs.acs.get_total_pop", return_value=SENTINEL_DF) as mock_fn:
        get_acs_data("TOTAL_POP", "2022", "county", as_percent=True)
        mock_fn.assert_called_once_with("2022", "county", True)


def test_enum_value_resolves():
    from fedwrap.census_acs.config import MeasureID
    with patch("fedwrap.census_acs.acs.get_race", return_value=SENTINEL_DF) as mock_fn:
        get_acs_data(MeasureID.RACE, "2022", "county")
        mock_fn.assert_called_once()


def test_unknown_measure_raises_value_error():
    with pytest.raises(ValueError, match="NOT_A_MEASURE"):
        get_acs_data("NOT_A_MEASURE", "2022", "county")


def test_all_map_values_are_callable():
    for key, func in measure_function_map.items():
        assert callable(func), f"Value for key '{key}' is not callable"
