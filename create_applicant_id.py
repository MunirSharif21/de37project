from cleaning_functions import *
import re
import pandas as pd
from datetime import datetime
# from extract_columns_into_new_table import *

##########
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
##########

df4 = get_clean_DF4(k="Talent/May2019Applicants.csv")
k = "Talent/May2019Applicants.csv"
# df2 = get_clean_DF2()


# print(df4)


def get_month_year_id_index(num):
    # find the year by getting a list of all consecutive numbers
    # let the first consecutive numbers represent the year
    y = re.findall(r"\d+", num)
    start_ind = 0
    end_ind = 0
    # get start and end point of the month in the key
    while not num[end_ind].isdigit():
        end_ind += 1
        if num[end_ind] == "/":
            start_ind = end_ind + 1
        if end_ind >= len(num):
            break
    # extract the string with the month, hence convert to date object
    mon = num[start_ind:start_ind+3]
    try:
        mon = datetime.strptime(mon, "%b")
    except ValueError:
        mon = datetime.strptime(mon, "%B")

    return int(y[0]), mon.month


def insert_base_id(df, name_of_file_in_aws):
    # set the old index as new column, rename and get the year/month integers
    df = df.reset_index()
    df = df.rename(columns={"index": "applicant_id"})
    y, m = get_month_year_id_index(name_of_file_in_aws)
    # print(y, m)

    # set the new index into the new format with 2-digit year,
    # 2-digit month, followed by 4-digit row index

    for i in range(df["applicant_id"].size):
        old_id = df.iloc[i, df.columns.get_loc("applicant_id")]
        new_id = (y % 1000) * 1000000
        new_id += m * 10000
        new_id += old_id
        df.iloc[i, df.columns.get_loc("applicant_id")] = new_id
    return df


