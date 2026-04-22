import pytest
import pandas as pd


@pytest.fixture
def fake_census_api_response():
    """Minimal Census API response: list-of-lists with header row."""
    return [["ucgid", "DP05_0001E"], ["geo123", "1234567"]]


@pytest.fixture
def fake_html_metadata_table():
    """Small HTML page with an ACS metadata table."""
    return """
    <html><body>
    <table>
      <tr><th>Name</th><th>Label</th><th>Concept</th></tr>
      <tr><th>col</th><th>col</th><th>col</th></tr>
      <tr><td>DP05_0001E</td><td>Estimate!!SEX AND AGE!!Total population</td><td>SEX AND AGE</td></tr>
      <tr><td>DP05_0002E</td><td>Estimate!!SEX AND AGE!!Total population!!Male</td><td>SEX AND AGE</td></tr>
    </table>
    </body></html>
    """


@pytest.fixture
def fake_places_response():
    """DataFrame mimicking a PLACES JSON API county response."""
    return pd.DataFrame({
        "measureid": ["ARTHRITIS", "ARTHRITIS"],
        "locationid": ["01001", "01003"],
        "stateabbr": ["AL", "AL"],
        "data_value": ["12.5", "15.0"],
        "datavaluetypeid": ["CrdPrv", "CrdPrv"],
    })


@pytest.fixture
def fake_brfss_response():
    """DataFrame mimicking a raw BRFSS API response."""
    return pd.DataFrame({
        "locationabbr": ["AL", "AL", "AK", "AK"],
        "response": ["Yes", "No", "Yes", "No"],
        "data_value": ["60.5", "39.5", "55.0", "45.0"],
        "break_out": ["Overall", "Overall", "Overall", "Overall"],
        "break_out_category": ["Overall", "Overall", "Overall", "Overall"],
        "year": ["2022", "2022", "2022", "2022"],
        "questionid": ["CHECKUP1", "CHECKUP1", "CHECKUP1", "CHECKUP1"],
    })


@pytest.fixture
def fake_svi_csv_content():
    """Small CSV string with SVI columns for two states."""
    return (
        "ST_ABBR,STCNTY,RPL_THEMES\n"
        "MD,24001,0.5\n"
        "VA,51001,0.3\n"
    )


@pytest.fixture(scope="session")
def tmp_cache_dir(tmp_path_factory):
    """Isolated temp directory for SVI cache tests."""
    return tmp_path_factory.mktemp("svi_cache")
