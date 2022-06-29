import pandas as pd
import numpy as np
from datetime import datetime

"""
This file contains common functions for cleaning various aspects of the dataframes
These functions are generic
"""


def delete_column(df, col_name):
    df = df.drop(columns=col_name)
    return df


def apply_to_each_row_in_column(df, col_name, function, not_dict=True):
    # apply a specific function mapping to each row in a specified column
    # if the value is Null, set the value as NA for consistency
    for row in range(df[col_name].size):
        old_value = df.iloc[row, df.columns.get_loc(col_name)]
        if pd.isnull(old_value):
            new_value = np.nan
        else:
            # if a function is used, use round brackets, if dict, use square
            if not_dict:
                new_value = function(old_value)
            else:
                new_value = function[old_value]
        df.iloc[row, df.columns.get_loc(col_name)] = new_value
    return df


def split_name_into_3(df, col_name="name"):
    first_names = []
    middle_names = []
    last_names = []
    for i in range(0, df[col_name].size):
        try:
            full_name = df.iloc[i, df.columns.get_loc(col_name)]
            all_names = full_name.split()
            first_names.append(all_names[0])

            if len(all_names) == 2:
                middle_names.append(" ")
                last_names.append(all_names[1])
            else:
                middle_names.append("".join(all_names[1:-1]))
                last_names.append(all_names[-1])
        except IndexError:
            print(i)
    df.insert(1, "first_name", first_names)
    df.insert(2, "middle_names", middle_names)
    df.insert(3, "last_name", last_names)
    # print(first_names)
    # print(last_names)
    df = df.drop(columns=col_name)
    return df


def split_name_into_2(df, col_name="name"):
    first_names = []
    last_names = []
    for i in range(0, df[col_name].size):
        try:
            full_name = df.iloc[i, df.columns.get_loc(col_name)]
            all_names = full_name.split()
            first_names.append(all_names[0])
            last_names.append("".join(all_names[1:]))
        except IndexError:
            print(i)
    df.insert(1, "first_name", first_names)
    df.insert(2, "last_names", last_names)
    # print(first_names)
    # print(last_names)
    df = df.drop(columns=col_name)
    return df


def clean_phone_numbers(num):
    # filter out the specified characters
    num = str(num)
    filter_list = ["+", "-", " ", "(", ")"]
    for f in filter_list:
        num = num.replace(f, "")
    return num


def change_date_to_ymd(old_date):
    temp_date = datetime.strptime(old_date, "%d/%m/%Y")
    new_date = temp_date.strftime("%Y/%m/%d")
    return new_date


def clean_month_column(old_date):
    # use only the first 3 letters and the last 4 digits
    # this allows datetime to get month and year
    extract_month_year = old_date[:3] + "/" + old_date[-4:]
    temp_date = datetime.strptime(extract_month_year, "%b/%Y")
    new_date = temp_date.strftime("%m/%Y")
    return new_date


def clean_invited_date(old_date):
    # remove decimal point and set as string for datetime to work
    extract_day = str(int(old_date))
    temp_date = datetime.strptime(extract_day, "%d")
    new_date = temp_date.strftime("%d")
    return new_date


def fix_spelling(name):
    if name == "Bruno Bellbrook":
        return "Bruno Belbrook"
    if name == "Fifi Eton":
        return "Fifi Etton"
    return name


def removeFraction(value):
    for i, v in enumerate(value):
        if v == "/":
            return value[:i]


def removeAcademyWord(value):
    value = value.replace("Academy", "")
    return value


def fix_index(df0):
    df0 = df0.reset_index()
    df0 = df0.drop(columns="index")
    return df0


def fix_double_slash(value):
    value = value.replace("//", "/")
    return value


def combine_date_month(df):
    df["invited_date"] = df["invited_date"] + "/" + df["month"]
    return df


def swap_specific_columns(df, index_1, index_2):
    col_list = list(df)
    col_list[index_1], col_list[index_2] = col_list[index_2], col_list[index_1]
    df.columns = col_list
    return df


