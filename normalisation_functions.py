import pandas as pd
from clean_functions import apply_to_each_row_in_column

"""
This file contains functions for normalisation
"""


def normalise(df, col_names, index=None, deletion=False, old_id=False, new_id=False):
    """
    This fancy function takes a dataframe and extracts the specified columns into a new dataframe
    Then it performs a number of operations based on the selected settings:
    :param df: Original Table to be used
    :param col_names: Columns from the table to be extracted
    :param index: Column used for ID *if* no new ID is generated
    :param deletion: Should the extracted columns be deleted?,
    :param old_id: Should old ID be used?,
    :param new_id: Should a new ID be made?,
    :return: Original table and the new table
    """
    new_df = df[col_names]

    if old_id:
        new_df = pd.concat([df[index], new_df], axis=1)

    elif new_id:
        new_df, key_mapping = generate_new_ids(new_df, index)
        df = apply_to_each_row_in_column(df, "invited_by", key_mapping, not_dict=False)

    if deletion:
        df = df.drop(columns=col_names)

    return df, new_df


def generate_new_ids(df, column_name):
    unique_values = {}

    # find all the unique values, hence convert into dataframe
    for row in range(df[column_name].size):
        old_value = df.iloc[row, df.columns.get_loc(column_name)]
        unique_values[old_value] = 1
    df_set = pd.DataFrame.from_dict(unique_values, orient="index")

    # remove na, fix index, drop redundant column
    df_set = df_set.dropna()
    df_set = df_set.reset_index()
    df_set = df_set.rename(columns={"index": column_name})
    df_set = df_set.drop(columns=0)
    df_set = df_set.dropna()
    df_set = df_set.reset_index()
    df_set = df_set.drop(columns="index")
    df_set = df_set.reset_index()
    df_set = df_set.rename(columns={"index": "id"})

    # create a map for the values in the original table to replace the values there
    key_mapping = df_set.to_dict()[column_name]
    # swap keys and values
    key_mapping = dict((v, k) for k, v in key_mapping.items())

    return df_set, key_mapping
