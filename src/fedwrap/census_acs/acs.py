from fedwrap.census_acs.DP02_functions import get_household_type, get_household_relationship, get_male_marital_status, get_female_marital_status, get_school_enrollment, get_educational_attainment, get_veteran_status, get_residence_year_ago, get_place_of_birth, get_US_citizenship_status, get_world_region_of_birth_of_foreign_born, get_language_spoken_at_home, get_ancestry, get_computer_and_internet_use
from fedwrap.census_acs.DP03_functions import get_employment_status, get_commuting_to_work, get_occupation, get_industry, get_class_of_worker, get_household_income, get_households_with_earnings, get_households_with_social_security, get_households_with_retirement_income, get_households_with_supplemental_security_income, get_households_with_cash_public_assistance_income, get_households_with_SNAP_benefits, get_family_income, get_health_insurance_coverage
from fedwrap.census_acs.DP04_functions import get_housing_occupancy, get_units_in_structure, get_year_structure_built, get_rooms, get_bedrooms, get_housing_tenure, get_year_householder_moved_into_unit, get_vehicles_available, get_house_heating_fuel, get_housing_lacking_complete_plumbing_facilities, get_housing_lacking_complete_kitchen_facilities, get_housing_no_telephone_service_available, get_occupants_per_room, get_housing_value, get_mortgage_status, get_selected_monthly_owner_costs_with_mortgage, get_selected_monthly_owner_costs_without_mortgage, get_SMOCAPI_with_mortgage, get_SMOCAPI_without_mortgage, get_gross_rent, get_GRAPI
from fedwrap.census_acs.DP05_functions import get_total_pop, get_pop_sex, get_age, get_race

# Define your mapping once
measure_function_map = {
    "HOUSEHOLD_TYPE": get_household_type,
    "HOUSEHOLD_RELATIONSHIP": get_household_relationship,
    "MALE_MARITAL_STATUS": get_male_marital_status,
    "FEMALE_MARITAL_STATUS": get_female_marital_status,
    "SCHOOL_ENROLLMENT": get_school_enrollment,
    "EDUCATIONAL_ATTAINMENT": get_educational_attainment,
    "VETERAN_STATUS": get_veteran_status,
    "RESIDENCE_YEAR_AGO": get_residence_year_ago,
    "PLACE_OF_BIRTH": get_place_of_birth,
    "US_CITIZENSHIP_STATUS": get_US_citizenship_status,
    "WORLD_REGION_OF_BIRTH_OF_FOREIGN_BORN": get_world_region_of_birth_of_foreign_born,
    "LANGUAGE_SPOKEN_AT_HOME": get_language_spoken_at_home,
    "ANCESTRY": get_ancestry,
    "COMPUTER_AND_INTERNET_USE": get_computer_and_internet_use,
    "EMPLOYMENT_STATUS": get_employment_status,
    "COMMUTING_TO_WORK": get_commuting_to_work,
    "OCCUPATION": get_occupation,
    "INDUSTRY": get_industry,
    "CLASS_OF_WORKER": get_class_of_worker,
    "HOUSEHOLD_INCOME": get_household_income,
    "HOUSEHOLDS_WITH_EARNINGS": get_households_with_earnings,
    "HOUSEHOLDS_WITH_SOCIAL_SECURITY": get_households_with_social_security,
    "HOUSEHOLDS_WITH_RETIREMENT_INCOME": get_households_with_retirement_income,
    "HOUSEHOLDS_WITH_SUPPLEMENTAL_SECURITY_INCOME": get_households_with_supplemental_security_income,
    "HOUSEHOLDS_WITH_CASH_PUBLIC_ASSISTANCE_INCOME": get_households_with_cash_public_assistance_income,
    "HOUSEHOLDS_WITH_SNAP_BENEFITS": get_households_with_SNAP_benefits,
    "FAMILY_INCOME": get_family_income,
    "HEALTH_INSURANCE_COVERAGE": get_health_insurance_coverage,
    "HOUSING_OCCUPANCY": get_housing_occupancy,
    "UNITS_IN_STRUCTURE": get_units_in_structure,
    "YEAR_STRUCTURE_BUILT": get_year_structure_built,
    "ROOMS": get_rooms,
    "BEDROOMS": get_bedrooms,
    "HOUSING_TENURE": get_housing_tenure,
    "YEAR_HOUSEHOLDER_MOVED_INTO_UNIT": get_year_householder_moved_into_unit,
    "VEHICLES_AVAILABLE": get_vehicles_available,
    "HOUSE_HEATING_FUEL": get_house_heating_fuel,
    "HOUSING_LACKING_COMPLETE_PLUMBING_FACILITIES": get_housing_lacking_complete_plumbing_facilities,
    "HOUSING_LACKING_COMPLETE_KITCHEN_FACILITIES": get_housing_lacking_complete_kitchen_facilities,
    "HOUSING_NO_TELEPHONE_SERVICE_AVAILABLE": get_housing_no_telephone_service_available,
    "OCCUPANTS_PER_ROOM": get_occupants_per_room,
    "HOUSING_VALUE": get_housing_value,
    "MORTGAGE_STATUS": get_mortgage_status,
    "SELECTED_MONTHLY_OWNER_COSTS_WITH_MORTGAGE": get_selected_monthly_owner_costs_with_mortgage,
    "SELECTED_MONTHLY_OWNER_COSTS_WITHOUT_MORTGAGE": get_selected_monthly_owner_costs_without_mortgage,
    "SMOCAPI_WITH_MORTGAGE": get_SMOCAPI_with_mortgage,
    "SMOCAPI_WITHOUT_MORTGAGE": get_SMOCAPI_without_mortgage,
    "GROSS_RENT": get_gross_rent,
    "GRAPI": get_GRAPI,
    "TOTAL_POP": get_total_pop,
    "POP_SEX": get_pop_sex,
    "AGE": get_age,
    "RACE": get_race,
}


def get_acs_data(measureid, year, geo, as_percent=False):

    func = measure_function_map.get(measureid)
    if func:
        return func(year, geo, as_percent)
    else:
        raise ValueError(f"Unknown measure ID: {measureid}")