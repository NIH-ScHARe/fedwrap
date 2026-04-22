"""
Tests for pure functions in svi_utils.py — no filesystem or network access needed.
"""
import io
import pytest
import pandas as pd

from fedwrap.cdc_svi.svi_utils import _build_url, _load_svi_csv, _filter_state

# All registered (year, geography) combinations
REGISTERED_COMBOS = [
    (2022, "tract"), (2022, "county"), (2022, "ZCTA"),
    (2020, "tract"), (2020, "county"),
    (2018, "tract"), (2018, "county"),
    (2016, "tract"), (2016, "county"),
    (2014, "tract"), (2014, "county"),
    (2010, "tract"), (2010, "county"),
    (2000, "tract"), (2000, "county"),
]


# ---------------------------------------------------------------------------
# _build_url
# ---------------------------------------------------------------------------

def test_build_url_returns_https_string():
    url = _build_url(2022, "tract")
    assert isinstance(url, str) and url.startswith("https://")


def test_build_url_contains_year():
    url = _build_url(2022, "county")
    assert "2022" in url


def test_build_url_unknown_combination_raises_value_error():
    with pytest.raises(ValueError, match="No SVI file registered"):
        _build_url(1999, "tract")


def test_build_url_all_registered_combinations_return_strings():
    for year, geo in REGISTERED_COMBOS:
        url = _build_url(year, geo)
        assert isinstance(url, str) and url.startswith("https://"), \
            f"Bad URL for ({year}, {geo})"


# ---------------------------------------------------------------------------
# _load_svi_csv
# ---------------------------------------------------------------------------

def _write_csv(tmp_path, content, filename="svi.csv"):
    p = tmp_path / filename
    p.write_text(content)
    return p


def test_load_svi_csv_reads_all_rows(tmp_path):
    csv = "ST_ABBR,STCNTY\nMD,24001\nVA,51001\n"
    path = _write_csv(tmp_path, csv)
    df = _load_svi_csv(path, 2022)
    assert len(df) == 2


def test_load_svi_csv_year_2000_skips_first_row(tmp_path):
    # First row is extraneous header; real header is second row
    csv = "EXTRA HEADER ROW\nST_ABBR,STCNTY\nMD,24001\n"
    path = _write_csv(tmp_path, csv)
    df = _load_svi_csv(path, 2000)
    assert "ST_ABBR" in df.columns
    assert len(df) == 1


def test_load_svi_csv_all_columns_are_strings(tmp_path):
    csv = "ST_ABBR,STCNTY,RPL_THEMES\nMD,24001,0.5\n"
    path = _write_csv(tmp_path, csv)
    df = _load_svi_csv(path, 2022)
    for col in df.columns:
        assert df[col].dtype == object, f"Column {col} is not dtype object (str)"


# ---------------------------------------------------------------------------
# _filter_state
# ---------------------------------------------------------------------------

@pytest.fixture
def two_state_df():
    return pd.DataFrame({
        "ST_ABBR": ["MD", "MD", "VA"],
        "STCNTY": ["24001", "24003", "51001"],
        "RPL_THEMES": ["0.5", "0.6", "0.3"],
    })


@pytest.fixture
def two_state_df_2010():
    return pd.DataFrame({
        "STATE_ABBR": ["MD", "VA"],
        "STCNTY": ["24001", "51001"],
    })


def test_filter_state_none_returns_all_rows(two_state_df):
    result = _filter_state(two_state_df, None, 2022)
    assert len(result) == 3


def test_filter_state_filters_to_matching_state(two_state_df):
    result = _filter_state(two_state_df, "MD", 2022)
    assert len(result) == 2
    assert all(result["ST_ABBR"] == "MD")


def test_filter_state_uses_state_abbr_for_2010(two_state_df_2010):
    result = _filter_state(two_state_df_2010, "MD", 2010)
    assert len(result) == 1
    assert result["STATE_ABBR"].iloc[0] == "MD"


def test_filter_state_uses_st_abbr_for_2022(two_state_df):
    result = _filter_state(two_state_df, "VA", 2022)
    assert len(result) == 1
    assert result["ST_ABBR"].iloc[0] == "VA"


def test_filter_state_nonexistent_state_returns_empty(two_state_df):
    result = _filter_state(two_state_df, "ZZ", 2022)
    assert len(result) == 0
