from enum import Enum 
from typing import Literal

Year = Literal[
    2018, 2019, 2020, 2021, 2022
]

class Geography(str, Enum):
    COUNTY = "county"
    CENSUS = "census"
    ZCTA = "zcta"
    PLACES = "places"

class MeasureType(str, Enum):
    CRUDE = "CrdPrv"
    AGE_ADJUSTED = "AgeAdjPrv"

class MeasureID(str, Enum):
    ARTHRITIS = "ARTHRITIS"
    BPHIGH = "BPHIGH"
    CANCER = "CANCER"
    CASTHMA = "CASTHMA"
    CHD = "CHD"
    COPD = "COPD"
    DEPRESSION = "DEPRESSION"
    DIABETES = "DIABETES"
    HIGHCHOL = "HIGHCHOL"
    KIDNEY = "KIDNEY"
    OBESITY = "OBESITY"
    STROKE = "STROKE"
    TEETHLOST = "TEETHLOST"
    BINGE = "BINGE"
    CSMOKING = "CSMOKING"
    LPA = "LPA"
    SLEEP = "SLEEP"
    GHLTH = "GHLTH"
    MHLTH = "MHLTH"
    PHLTH = "PHLTH"
    ACCESS2 = "ACCESS2"
    BPMED = "BPMED"
    CERVICAL = "CERVICAL"
    CHECKUP = "CHECKUP"
    CHOLSCREEN = "CHOLSCREEN"
    COLON_SCREEN = "COLON_SCREEN"
    COREM = "COREM"
    COREW = "COREW"
    DENTAL = "DENTAL"
    MAMMOUSE = "MAMMOUSE"
    HEARING = "HEARING"
    VISION = "VISION"
    COGNITION = "COGNITION"
    MOBILITY = "MOBILITY"
    SELFCARE = "SELFCARE"
    INDEPLIVE = "INDEPLIVE"
    DISABILITY = "DISABILITY"
    ISOLATION = "ISOLATION"
    FOODSTAMP = "FOODSTAMP"
    FOODINSECU = "FOODINSECU"
    HOUSINSECU = "HOUSINSECU"
    SHUTUTILITY = "SHUTUTILITY"
    LACKTRPT = "LACKTRPT"
    EMOTIONSPT = "EMOTIONSPT"

# API Endpoints 
DATA_DICTIONARY_ENDPOINT = "https://data.cdc.gov/resource/m35w-spkz.json"

API_ENDPOINTS = {
    "county": {
        "places_release_2024": "https://data.cdc.gov/resource/swc5-untb.json",
        "places_release_2023": "https://data.cdc.gov/resource/h3ej-a9ec.json",
        "places_release_2022": "https://data.cdc.gov/resource/duw2-7jbt.json",
        "places_release_2021": "https://data.cdc.gov/resource/pqpp-u99h.json",
        "places_release_2020": "https://data.cdc.gov/resource/dv4u-3x3q.json",
    },
    "census": {
        "places_release_2024": "https://data.cdc.gov/resource/cwsq-ngmh.json",
        "places_release_2023": "https://data.cdc.gov/resource/em5e-5hvn.json",
        "places_release_2022": "https://data.cdc.gov/resource/nw2y-v4gm.json",
        "places_release_2021": "https://data.cdc.gov/resource/373s-ayzu.json",
        "places_release_2020": "https://data.cdc.gov/resource/4ai3-zynv.json",
    },
    "zcta": {
        "places_release_2024": "https://data.cdc.gov/resource/qnzd-25i4.json",
        "places_release_2023": "https://data.cdc.gov/resource/9umn-c3jf.json",
        "places_release_2022": "https://data.cdc.gov/resource/gd4x-jyhw.json",
        "places_release_2021": "https://data.cdc.gov/resource/s85h-9xpy.json",
        "places_release_2020": "https://data.cdc.gov/resource/fbbf-hgkc.json",
    },
    "places": {
        "places_release_2024": "https://data.cdc.gov/resource/eav7-hnsx.json",
        "places_release_2023": "https://data.cdc.gov/resource/krqc-563j.json",
        "places_release_2022": "https://data.cdc.gov/resource/epbn-9bv3.json",
        "places_release_2021": "https://data.cdc.gov/resource/q8ig-wwk9.json",
        "places_release_2020": "https://data.cdc.gov/resource/q8xq-ygsk.json",
    }
}
