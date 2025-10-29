import ipywidgets as w
from IPython.display import display

VARIABLE_CATALOG: dict[str, list[str]] = {
    "ACS": [
        "HOUSEHOLD_TYPE",
        "HOUSEHOLD_RELATIONSHIP",
        "MALE_MARITAL_STATUS",
        "FEMALE_MARITAL_STATUS",
        "SCHOOL_ENROLLMENT",
        "EDUCATIONAL_ATTAINMENT",
        "VETERAN_STATUS",
        "RESIDENCE_YEAR_AGO",
        "PLACE_OF_BIRTH",
        "US_CITIZENSHIP_STATUS",
        "WORLD_REGION_OF_BIRTH_OF_FOREIGN_BORN",
        "LANGUAGE_SPOKEN_AT_HOME",
        "ANCESTRY",
        "COMPUTER_AND_INTERNET_USE",
        "EMPLOYMENT_STATUS",
        "COMMUTING_TO_WORK",
        "OCCUPATION",
        "INDUSTRY",
        "CLASS_OF_WORKER",
        "HOUSEHOLD_INCOME",
        "HOUSEHOLDS_WITH_EARNINGS",
        "HOUSEHOLDS_WITH_SOCIAL_SECURITY",
        "HOUSEHOLDS_WITH_RETIREMENT_INCOME",
        "HOUSEHOLDS_WITH_SUPPLEMENTAL_SECURITY_INCOME",
        "HOUSEHOLDS_WITH_CASH_PUBLIC_ASSISTANCE_INCOME",
        "HOUSEHOLDS_WITH_SNAP_BENEFITS",
        "FAMILY_INCOME",
        "HEALTH_INSURANCE_COVERAGE",
        "HOUSING_OCCUPANCY",
        "UNITS_IN_STRUCTURE",
        "YEAR_STRUCTURE_BUILT",
        "ROOMS",
        "BEDROOMS",
        "HOUSING_TENURE",
        "YEAR_HOUSEHOLDER_MOVED_INTO_UNIT",
        "VEHICLES_AVAILABLE",
        "HOUSE_HEATING_FUEL",
        "HOUSING_LACKING_COMPLETE_PLUMBING_FACILITIES",
        "HOUSING_LACKING_COMPLETE_KITCHEN_FACILITIES",
        "HOUSING_NO_TELEPHONE_SERVICE_AVAILABLE",
        "OCCUPANTS_PER_ROOM",
        "HOUSING_VALUE",
        "MORTGAGE_STATUS",
        "SELECTED_MONTHLY_OWNER_COSTS_WITH_MORTGAGE",
        "SELECTED_MONTHLY_OWNER_COSTS_WITHOUT_MORTGAGE",
        "SMOCAPI_WITH_MORTGAGE",
        "SMOCAPI_WITHOUT_MORTGAGE",
        "GROSS_RENT",
        "GRAPI",
        "TOTAL_POP",
        "POP_SEX",
        "AGE",
        "RACE",
    ],
    "CDC PLACES": [
        "ARTHRITIS",
        "BPHIGH",
        "CANCER",
        "CASTHMA",
        "CHD",
        "COPD",
        "DEPRESSION",
        "DIABETES",
        "HIGHCHOL",
        "KIDNEY",
        "OBESITY",
        "STROKE",
        "TEETHLOST",
        "BINGE",
        "CSMOKING",
        "LPA",
        "SLEEP",
        "GHLTH",
        "MHLTH",
        "PHLTH",
        "ACCESS2",
        "BPMED",
        "CERVICAL",
        "CHECKUP",
        "CHOLSCREEN",
        "COLON_SCREEN",
        "COREM",
        "COREW",
        "DENTAL",
        "MAMMOUSE",
        "HEARING",
        "VISION",
        "COGNITION",
        "MOBILITY",
        "SELFCARE",
        "INDEPLIVE",
        "DISABILITY",
        "ISOLATION",
        "FOODSTAMP",
        "FOODINSECU",
        "HOUSINSECU",
        "SHUTUTILITY",
        "LACKTRPT",
        "EMOTIONSPT"
    ],
    "CDC BRFSS": [  # ← rename to your actual third dataset ID
        "VAR_A",
        "VAR_B",
        "VAR_C",
    ],
}

class Explorer:
    """A small, dependency-light ipywidgets app."""

    def __init__(self):
        ds_ids = list(VARIABLE_CATALOG.keys())

        self.dataset = w.Dropdown(
            options=ds_ids,
            value=ds_ids[0],
            description="Dataset",
        )

        self.variable = w.Dropdown(
            options=VARIABLE_CATALOG[self.dataset.value],
            description="Variable",
        )
    
        # (Optional) A label showing the current selection
        self.selection = w.HTML()

        # Wire events
        self.dataset.observe(self._on_dataset_change, names="value")
        self.variable.observe(self._on_variable_change, names="value")

        self.root = w.VBox(
            [
                w.HTML("<h3>Federal Data – Quick Picker</h3>"),
                self.dataset,
                self.variable,
                self.selection,
            ]
        )

        # Initialize label
        self._update_selection_label()

    # Auto-display in notebooks when the object is the last expression
    # def _ipython_display_(self):
    #     display(self.root)

    def _on_dataset_change(self, change):
        ds = change["new"]
        # Update the variable dropdown options to match the dataset
        vars_for_ds = VARIABLE_CATALOG.get(ds, [])
        # Preserve value if still valid, else fall back to first option
        new_value = self.variable.value if self.variable.value in vars_for_ds else (vars_for_ds[0] if vars_for_ds else None)
        self.variable.options = vars_for_ds
        self.variable.value = new_value
        self._update_selection_label()

    def _on_variable_change(self, _):
        self._update_selection_label()

    def _update_selection_label(self):
        ds = self.dataset.value
        var = self.variable.value
        self.selection.value = (
            f"<b>Selected:</b> {ds}" + (f" → <code>{var}</code>" if var else "")
        )

def display_explorer() -> Explorer:
    """Build and display the explorer; return the object for further use."""
    ui = Explorer()
    display(ui.root)
    return ui