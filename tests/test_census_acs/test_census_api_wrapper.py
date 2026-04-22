import pytest
from unittest.mock import patch, MagicMock
import pandas as pd

from fedwrap.census_acs.census_API_wrapper import (
    get_variable_name,
    extract_label_name,
    get_ACS_url,
    get_api_dataframe,
)


# ---------------------------------------------------------------------------
# get_variable_name
# ---------------------------------------------------------------------------

@pytest.fixture
def metadata_table():
    return pd.DataFrame({
        "Name": ["DP05_0001E", "DP05_0002E", "DP05_0003E"],
        "Label": [
            "Estimate!!SEX AND AGE!!Total population",
            "Estimate!!SEX AND AGE!!Total population!!Male",
            "Estimate!!SEX AND AGE!!Total population!!Male",  # duplicate label
        ],
    })


def test_get_variable_name_returns_match(metadata_table):
    result = get_variable_name(metadata_table, "Estimate!!SEX AND AGE!!Total population")
    assert result == "DP05_0001E"


def test_get_variable_name_returns_none_when_not_found(metadata_table):
    result = get_variable_name(metadata_table, "Nonexistent!!Label")
    assert result is None


def test_get_variable_name_return_index_selects_second_match(metadata_table):
    result = get_variable_name(
        metadata_table,
        "Estimate!!SEX AND AGE!!Total population!!Male",
        return_index=1,
    )
    assert result == "DP05_0003E"


def test_get_variable_name_single_match_ignores_return_index(metadata_table):
    result = get_variable_name(
        metadata_table,
        "Estimate!!SEX AND AGE!!Total population",
        return_index=5,
    )
    assert result == "DP05_0001E"


# ---------------------------------------------------------------------------
# extract_label_name
# ---------------------------------------------------------------------------

def test_extract_label_name_prepends_ucgid():
    result = extract_label_name(["Estimate!!SEX AND AGE!!Total population"])
    assert result[0] == "ucgid"


def test_extract_label_name_splits_on_double_bang():
    result = extract_label_name(["Estimate!!SEX AND AGE!!Male"])
    assert result[1] == "Male"


def test_extract_label_name_empty_input_returns_only_ucgid():
    result = extract_label_name([])
    assert result == ["ucgid"]


def test_extract_label_name_multiple_labels():
    result = extract_label_name(["A!!B!!Male", "A!!B!!Female"])
    assert result == ["ucgid", "Male", "Female"]


# ---------------------------------------------------------------------------
# get_ACS_url
# ---------------------------------------------------------------------------

def test_get_acs_url_contains_year_and_table():
    url = get_ACS_url("2022", "DP05", "county")
    assert "2022" in url
    assert "DP05" in url


def test_get_acs_url_all_geo_keys_produce_urls():
    geos = ["country", "state", "county", "census tract", "zip code",
            "congressional district", "MSA"]
    for geo in geos:
        url = get_ACS_url("2022", "DP05", geo)
        assert isinstance(url, str) and url.startswith("https://"), f"Bad URL for geo={geo}"


def test_get_acs_url_unknown_geo_produces_none_string():
    # get_ACS_url uses .get() on the map, so unknown geo interpolates None
    url = get_ACS_url("2022", "DP05", "unknown_geo")
    assert "None" in url


# ---------------------------------------------------------------------------
# get_api_dataframe
# ---------------------------------------------------------------------------

def test_get_api_dataframe_first_row_becomes_headers():
    mock_response = MagicMock()
    mock_response.json.return_value = [["col_a", "col_b"], ["1", "2"]]

    with patch("fedwrap.census_acs.census_API_wrapper.requests.get", return_value=mock_response):
        df = get_api_dataframe("https://fake.url")

    assert list(df.columns) == ["col_a", "col_b"]
    assert len(df) == 1


def test_get_api_dataframe_values_are_strings():
    mock_response = MagicMock()
    mock_response.json.return_value = [["ucgid", "val"], ["geo1", "42"]]

    with patch("fedwrap.census_acs.census_API_wrapper.requests.get", return_value=mock_response):
        df = get_api_dataframe("https://fake.url")

    assert df["val"].iloc[0] == "42"
