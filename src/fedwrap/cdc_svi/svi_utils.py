import requests
import os
from pathlib import Path
import pandas as pd

def _build_url(year: int, geography: str) -> str:

    SVI_FILES = {
        # (year, geography) -> filename or URL
        (2022, "tract"):  "https://svi.cdc.gov/Documents/Data/2022/csv/states/SVI_2022_US.csv",
        (2022, "county"): "https://svi.cdc.gov/Documents/Data/2022/csv/states_counties/SVI_2022_US_county.csv",
        (2022, "ZCTA"):  "https://svi.cdc.gov/Documents/Data/2022/csv/zcta/SVI_2022_US_ZCTA.csv",
        (2020, "tract"): "https://svi.cdc.gov/Documents/Data/2020/csv/states/SVI_2020_US.csv",
        (2020, "county"): "https://svi.cdc.gov/Documents/Data/2020/csv/states_counties/SVI_2020_US_county.csv",
        (2018, "county"): "https://svi.cdc.gov/Documents/Data/2018/csv/states_counties/SVI_2018_US_county.csv",
        (2018, "tract"): "https://svi.cdc.gov/Documents/Data/2018/csv/states/SVI_2018_US.csv",
        (2016, "county"): "https://svi.cdc.gov/Documents/Data/2016/csv/states_counties/SVI_2016_US_county.csv",
        (2016, "tract"): "https://svi.cdc.gov/Documents/Data/2016/csv/states/SVI_2016_US.csv",
        (2014, "county"): "https://svi.cdc.gov/Documents/Data/2014/csv/states_counties/SVI_2014_US_county.csv",
        (2014, "tract"): "https://svi.cdc.gov/Documents/Data/2014/csv/states/SVI_2014_US.csv",
        (2010, "county"): "https://svi.cdc.gov/Documents/Data/2010/csv/states_counties/SVI_2010_US_county.csv",
        (2010, "tract"): "https://svi.cdc.gov/Documents/Data/2010/csv/states/SVI_2010_US.csv",
        (2000, "county"): "https://svi.cdc.gov/Documents/Data/2000/csv/states_counties/SVI_2000_US_county.csv",
        (2000, "tract"): "https://svi.cdc.gov/Documents/Data/2000/csv/states/SVI_2000_US.csv"
    }

    try:
        fname = SVI_FILES[(year, geography)]
    except KeyError:
        raise ValueError(f"No SVI file registered for year={year}, geography={geography}")
    return f"{fname}"

def _download_if_needed(url: str, refresh: bool = False) -> Path:

    CACHE_DIR = Path(os.environ.get("MYPKG_CACHE_DIR", Path.home() / ".fedwrap" / "cdc_svi"))
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    fname = url.split("/")[-1]
    dest = CACHE_DIR / fname

    if dest.exists() and not refresh:
        return dest

    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return dest

def _load_svi_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str)  # keep IDs as strings

if __name__ == "__main__":
    url = _build_url(2010, "county")
    file_destination = _download_if_needed(url, refresh=True)
    df = _load_svi_csv(file_destination)
    print(df.head())