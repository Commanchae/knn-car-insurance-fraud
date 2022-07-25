from math import sqrt
import pandas as pd
import numpy as np
from pandas_helper import convert_categorical_to_numerical

insurance_df = pd.read_csv("car-insurance-fraud.csv")

# Renaming the columns to make them easier to work with.
columns_to_rename = {
    'Customer': 'customer',
    'Claim Amount ': 'claim_amount',
    'Coverage': 'coverage',
    'Education': 'education',
    'Employment Status': 'employment_status',
    'Gender': 'gender',
    'Annual Income ($)': 'annual_income_in_usd',
    'Location Category': 'location_category',
    'Marital Status': 'marital_status',
    'Age': 'age',
    'Monthly Premium': 'monthly_premium',
    'Months Since Last Claim': 'months_since_last_claim',
    'Vehicle Size': 'vehicle_size',
    'Reported to Police?': 'reported_to_police',
    'Witness Details provided?': 'witness_details_provided',
    'Weekend?': 'weekend',
    'Car driveable?': 'car_driveable',
    'Fraud Detected? Yes=1, No=0': 'fraud_detected'
}

insurance_df.rename(columns = columns_to_rename, inplace=True)

# Dropping irrelevant data.
insurance_df.drop(columns = ['customer'], axis=1, inplace=True)

# Turn categorical data into numericals.
for column in ['coverage', 'education', 'employment_status', 
            'gender', 'location_category', 'marital_status', 
            'vehicle_size', 'reported_to_police', 'witness_details_provided',
            'weekend', 'car_driveable']:
            insurance_df = convert_categorical_to_numerical(insurance_df, column)


# Shuffle and get the train/test set.
insurance_np = np.array(insurance_df)
np.random.shuffle(insurance_np)
TEST_SIZE = 0.2
dataframe_length = len(insurance_np)

train_set = insurance_np[0:int((1-TEST_SIZE)*dataframe_length)]
test_set = insurance_np[int((1-TEST_SIZE)*dataframe_length):]


# With train/test, get X_train, X_test, y_train, y_test.
X_train = train_set[:, 0:-2]
y_train = train_set[:,-1:]

X_test = test_set[:,0:-2]
y_test = test_set[:,-1:]

def euclidean_distance(data_one, data_two):
    dist = 0
    for i in range(len(data_one)):
        dist += (data_two[i] - data_one[i])**2
    dist = sqrt(dist)
    return dist

def k_nearest_neighbours(dataset, test_data, k=3):
    # Dataset
    '''
    [
        [   [FEATURES], [LABEL]   ],
        [   [FEATURES], [LABEL]   ],
    ]
    
    '''

    k_nearest_distance = []
    k_nearest_label = []
    for data in dataset:
        dist = euclidean_distance(data, test_data)
        if len(k_nearest_distance) < k:
            k_nearest_distance.append(dist)
            k_nearest_label.append(data[-1]) # Gets the label.
        else:
            max_dist =  max(k_nearest_distance)
            max_index = -1
            max_index = k_nearest_distance.index(max_dist)
            if dist < max_dist:
                k_nearest_distance[max_index] = dist
                k_nearest_label[max_index] = data[-1]

    label_count = {}
    for i in range(len(k_nearest_distance)):
        try:
            label_count[k_nearest_label[i]] += 1
        except Exception as e:
            label_count[k_nearest_label[i]] = 0

    # Get the max count.
    max_label = None
    max_count = 0
    for key in label_count:
        if label_count[key] > max_count:
            max_label = key
            max_count = label_count[key] 
    
    prediction = max_label
    return prediction, max_count/k

# Training the model.
data = X_train

# Test Accuracy
correct = 0
total = 0
for i in range(len(X_test)):
    total += 1
    prediction, confidence = k_nearest_neighbours(data, X_test[i], k = 10)
    if (prediction == y_test[i]):
        correct += 1
    
print("ACCURACY: ", correct/total)
# Finished with an accuracy of 79.8%

