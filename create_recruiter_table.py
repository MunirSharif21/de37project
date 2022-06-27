import pandas as pd

from extract_columns_into_new_table import *


def get_list_of_unique_trainers():
    dictionary = {}
    df_4 = get_clean_DF4()
    df_4, df_rec = extract_remove_columns(df_4, ["invited_by"], deletion=False)
    for i in range(df_rec["invited_by"].size):
        dictionary[df_rec.iloc[i][0]] = 1
    return dictionary


def dict_to_df():
    recruiter_list = get_list_of_unique_trainers()
    df_rec = pd.DataFrame.from_dict(recruiter_list, orient='index')
    df_rec = df_rec.reset_index()
    df_rec = df_rec.rename(columns={"index": "Full_name"})
    df_rec = df_rec.drop(columns=0)
    # remove Na
    df_rec = df_rec[1:]
    df_rec = split_name(df_rec, col_name="Full_name")
    return df_rec


def create_id(df):
    df = df.reset_index()
    df = df.rename(columns={"index": "recruiter_ID"})
    return df


# MAIN

recruiter_table = dict_to_df()
recruiter_table = create_id(recruiter_table)
# print(recruiter_table)
