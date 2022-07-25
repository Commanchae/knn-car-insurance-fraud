from pandas import DataFrame
import pandas as pd
from numpy import array

def convert_categorical_to_numerical(dataframe: DataFrame, column_name: str, replace: bool=False, return_dict: bool=False):
    '''
    Used to convert a given column of categorical values into numerics.

    The value given to each category depends on its order within the dataframe.

    With return_dict being True, the function returns the modified dataframe and a dictionary of the key,value pairs used.
    '''
    values = dataframe[column_name].values
    uniques = dataframe[column_name].unique()

    key_dictionary = {name: index for index, name in enumerate(uniques)}

    if replace:
        dataframe[column_name] = array([key_dictionary[value] for value in values])
    else:
        dataframe["n"+column_name] = array([key_dictionary[value] for value in values])    
    
    if return_dict:
        return dataframe, key_dictionary
    else:
        return dataframe

# def replace all values in a given column by giving it some values to replace with in a dictionary.
def replace_categorical(dataframe: DataFrame, column_name: str, values: dict):
    '''
    Takes in a dataframe, a column name of a categorical variable, and a dictionary containing the values to replace the categorical values to.

    In a column containing "yes" and "no", the values_dict can be passed through as
    {
        "yes": 1,
        "no": 0
    }
    To turn the values into 1's and 0's, respectively.
    '''
    df_values = dataframe[column_name].values
    values_uniques = [key for key in values]
    new_values = [values[value] if value in values_uniques else None for value in df_values]
    dataframe[column_name] = array(new_values)
    return dataframe


