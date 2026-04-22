"""
Integration tests for the get_svi public API function.
All private helpers are mocked so no network or filesystem access occurs.
"""
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import pandas as pd

from fedwrap.cdc_svi.main import get_svi

FAKE_PATH = Path("/tmp/fake_svi.csv")

TWO_STATE_DF = pd.DataFrame({
    "ST_ABBR": ["MD", "MD", "VA"],
    "STCNTY": ["24001", "24003", "51001"],
    "RPL_THEMES": ["0.5", "0.6", "0.3"],
})


@pytest.fixture
def patch_helpers():
    """Patch all private helpers used by get_svi."""
    with (
        patch("fedwrap.cdc_svi.main._build_url", return_value="https://fake.url") as mock_url,
        patch("fedwrap.cdc_svi.main._download_if_needed", return_value=FAKE_PATH) as mock_dl,
        patch("fedwrap.cdc_svi.main._load_svi_csv", return_value=TWO_STATE_DF.copy()) as mock_load,
        patch("fedwrap.cdc_svi.main._filter_state", return_value=TWO_STATE_DF.copy()) as mock_filter,
    ):
        yield {
            "build_url": mock_url,
            "download": mock_dl,
            "load": mock_load,
            "filter": mock_filter,
        }


def test_get_svi_returns_dataframe(patch_helpers):
    result = get_svi(2022)
    assert isinstance(result, pd.DataFrame)


def test_get_svi_refresh_forwarded_to_download(patch_helpers):
    get_svi(2022, refresh=True)
    patch_helpers["download"].assert_called_once_with("https://fake.url", refresh=True)


def test_get_svi_state_forwarded_to_filter(patch_helpers):
    get_svi(2022, state="MD")
    call_args = patch_helpers["filter"].call_args
    assert call_args[0][1] == "MD"  # second positional arg is state


def test_get_svi_state_none_passes_none_to_filter(patch_helpers):
    get_svi(2022, state=None)
    call_args = patch_helpers["filter"].call_args
    assert call_args[0][1] is None


def test_get_svi_with_state_filter_returns_subset(monkeypatch, tmp_path):
    """End-to-end with real _filter_state but mocked download."""
    csv_content = "ST_ABBR,STCNTY,RPL_THEMES\nMD,24001,0.5\nVA,51001,0.3\n"
    csv_file = tmp_path / "SVI_2022_US.csv"
    csv_file.write_text(csv_content)

    monkeypatch.setenv("MYPKG_CACHE_DIR", str(tmp_path))

    with (
        patch("fedwrap.cdc_svi.main._build_url", return_value="https://fake.url"),
        patch("fedwrap.cdc_svi.main._download_if_needed", return_value=csv_file),
    ):
        result = get_svi(2022, state="MD")

    assert all(result["ST_ABBR"] == "MD")
    assert len(result) == 1
