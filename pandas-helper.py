from ast import Str
from pandas import DataFrame
import pandas as pd
from pyparsing import col
from numpy import array

def convert_categorical_to_numerical(dataframe: DataFrame, column_name: Str, replace: bool=False, return_dict: bool=False):
    '''
    Used to convert a given column of categorical values into numerics.

    The value given to each category depends on its order within the dataframe.

    With return_dict being True, the function returns the modified dataframe and a dictionary of the key,value pairs used.
    '''
    values = dataframe[column_name].values
    uniques = dataframe[column_name].unique()

    key_dictionary = {name: index for index, name in enumerate(uniques)}

    if replace:
        dataframe.drop([column_name], axis=1, inplace=True)
        dataframe[column_name] = array([key_dictionary[value] for value in values])
    else:
        dataframe["n"+column_name] = array([key_dictionary[value] for value in values])    
    
    if return_dict:
        return dataframe, key_dictionary
    else:
        return dataframe

# def replace all values in a given column by giving it some values to replace with in a dictionary.