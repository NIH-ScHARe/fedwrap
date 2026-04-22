import pytest
from unittest.mock import patch, MagicMock, call
import pandas as pd
import requests

from fedwrap.cdc_places.places_utils import (
    query_api,
    get_release_for_year,
    get_endpoint_for_geo,
    get_places_data,
)


# ---------------------------------------------------------------------------
# query_api
# ---------------------------------------------------------------------------

def test_query_api_returns_dataframe_on_success():
    mock_resp = MagicMock()
    mock_resp.json.return_value = [{"col": "val"}]
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp):
        result = query_api("https://fake.url")
    assert isinstance(result, pd.DataFrame)
    assert "col" in result.columns


def test_query_api_always_sets_limit():
    mock_resp = MagicMock()
    mock_resp.json.return_value = []
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp) as mock_get:
        query_api("https://fake.url", params={"measureid": "ARTHRITIS"})
        _, kwargs = mock_get.call_args
        assert kwargs["params"]["$limit"] == 100000


def test_query_api_limit_set_even_with_no_params():
    mock_resp = MagicMock()
    mock_resp.json.return_value = []
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp) as mock_get:
        query_api("https://fake.url")
        _, kwargs = mock_get.call_args
        assert kwargs["params"]["$limit"] == 100000


def test_query_api_returns_none_on_request_exception():
    with patch(
        "fedwrap.cdc_places.places_utils.requests.get",
        side_effect=requests.RequestException("network error"),
    ):
        result = query_api("https://fake.url")
    assert result is None


# ---------------------------------------------------------------------------
# get_release_for_year
# ---------------------------------------------------------------------------

def _make_dict_response(measureid, year, release):
    """Build a minimal data-dictionary-style API response.

    The real CDC data dictionary uses release names as column headers and
    year strings as the cell values, so this mock mirrors that structure.
    """
    mock_resp = MagicMock()
    mock_resp.json.return_value = [
        {"measureid": measureid, release: str(year), "other_col": "foo"}
    ]
    return mock_resp


def test_get_release_for_year_returns_correct_release():
    mock_resp = _make_dict_response("ARTHRITIS", 2022, "places_release_2024")
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp):
        result = get_release_for_year("ARTHRITIS", 2022)
    assert result == "places_release_2024"


def test_get_release_for_year_returns_none_for_unknown_measureid():
    mock_resp = MagicMock()
    mock_resp.json.return_value = [{"measureid": "OTHER", "2022": "places_release_2024"}]
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp):
        result = get_release_for_year("NOTREAL", 2022)
    assert result is None


def test_get_release_for_year_returns_none_when_year_not_in_data():
    mock_resp = MagicMock()
    # Row exists but no column contains str(year) as a value
    mock_resp.json.return_value = [{"measureid": "ARTHRITIS", "2018": "places_release_2020"}]
    with patch("fedwrap.cdc_places.places_utils.requests.get", return_value=mock_resp):
        result = get_release_for_year("ARTHRITIS", 2099)
    assert result is None


# ---------------------------------------------------------------------------
# get_endpoint_for_geo
# ---------------------------------------------------------------------------

def test_get_endpoint_for_geo_returns_url_for_valid_inputs():
    result = get_endpoint_for_geo("county", "places_release_2024")
    assert isinstance(result, str) and result.startswith("https://")


def test_get_endpoint_for_geo_returns_none_for_unknown_geo():
    result = get_endpoint_for_geo("galaxy", "places_release_2024")
    assert result is None


def test_get_endpoint_for_geo_returns_none_for_missing_release():
    result = get_endpoint_for_geo("county", "places_release_1800")
    assert result is None


# ---------------------------------------------------------------------------
# get_places_data routing
# ---------------------------------------------------------------------------

def test_non_state_geo_calls_query_api():
    with (
        patch("fedwrap.cdc_places.places_utils.set_query_params", return_value=("https://fake.url", {})),
        patch("fedwrap.cdc_places.places_utils.query_api", return_value=pd.DataFrame()) as mock_qa,
    ):
        get_places_data("county", 2022, "ARTHRITIS")
        mock_qa.assert_called_once()


def test_state_geo_delegates_to_get_places_state_data():
    with patch(
        "fedwrap.cdc_places.places_utils.get_places_state_data",
        return_value=pd.DataFrame(),
    ) as mock_state:
        get_places_data("state", 2022, "ARTHRITIS")
        mock_state.assert_called_once_with(2022, "ARTHRITIS", "CrdPrv")
