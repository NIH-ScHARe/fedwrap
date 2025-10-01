from enum import Enum
from typing import Literal

Year = Literal[
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023
]

class Geography(str, Enum):
    STATE = "state"
    MSA = "msa"

class Measure(str, Enum):
    CRUDE = "crude"
    AGE_ADJUSTED = "age-adjusted"

class BreakOutCategory(str, Enum):
    OVERALL = "Overall"
    SEX = "Sex"
    AGE_GROUP = "Age Group"
    RACE_ETHNICITY = "Race/Ethnicity"
    EDUCATION = "Education Attained"
    INCOME = "Household Income" 

BRFSS_ENDPOINTS = {
    Geography.STATE: {
        Measure.CRUDE: "https://data.cdc.gov/resource/dttw-5yxu.json",
        Measure.AGE_ADJUSTED: "https://data.cdc.gov/resource/d2rk-yvas.json",
    },
    Geography.MSA: {
        Measure.CRUDE: "https://data.cdc.gov/resource/j32a-sa6u.json",
        Measure.AGE_ADJUSTED: "https://data.cdc.gov/resource/at7e-uhkc.json",
    },
    "questions": "https://data.cdc.gov/resource/iuq5-y9ct.json",
}
