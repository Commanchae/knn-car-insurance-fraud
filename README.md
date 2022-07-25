## Purpose
The purpose of this project is to apply the K-nearest-neighbors algorithm on a dataset regarding car insurance fraud claims in order to classify claims as either fradulent or non-fradulent based on the details of the claim. 

## About the Data 📖
The dataset was most likely modified from [Somnath Banerjee's kaggle dataset.](https://www.kaggle.com/datasets/somjee/auto-insurance-customerlifetimevalue/discussion) It was modified for use within Monash University Clayton's ETC1000 unit as teaching material. 

The dataset contains 18 columns, with a mix of categorical and discrete variables.

## Data Cleaning

The column names were changed to be easier to work with.
| Original Name | New Name |
| --------------|----------|
| Customer     | customer |
| Claim Amount  | claim_amount |
| Coverage      | coverage |
| Education     | education |
| Employment Status | employment_status |
| Gender | gender |
| Annual Income ($) | annual_income_in_usd |
| Location Category | location_category |
| Marital Status | marital_status |
| Age | age |
| Monthly Premium | monthly_premium |
| Months Since Last Claim | months_since_last_claim |
| Vehicle Size | vehicle_size |
| Reported to Police? | reported_to_police |
| Witness Details provided? | witness_details_provided |
| Weekend? | weekend |
| Car driveable? | car_driveable |
| Fraud Detected? Yes=1, No=0 | fraud_detected |

Please note that the column names were changed in code to make the change viewable.