from fedwrap.cdc_brfss.config import BRFSS_ENDPOINTS
from fedwrap.cdc_brfss.brfss_utils import api_call

url = BRFSS_ENDPOINTS["state"]["crude"]

# 4. Set params 
params = {
        "break_out_category" : "Overall",
        "locationabbr" : "AK"
    }

# 5. Make API call 
raw_df = api_call(url, params)

# get unique values of question column 
unique_questions = raw_df['question'].unique()

print(unique_questions)