import re
from datetime import datetime
import pickle


"""
This file provides functions needed to do specific changes to the frames
due to some weird behaviours by other files
"""


def convert_month_year_into_id(file_name):
    # find the year by getting a list of all consecutive numbers
    # let the first consecutive numbers represent the year
    year_name = re.findall(r"\d+", file_name)
    start_ind = 0
    end_ind = 0
    # get start and end point of the month in the key
    while not file_name[end_ind].isdigit():
        end_ind += 1
        if file_name[end_ind] == "/":
            start_ind = end_ind + 1
        if end_ind >= len(file_name):
            break
    # extract the string with the month, hence convert to date object
    month_name = file_name[start_ind:start_ind + 3]
    try:
        month_name = datetime.strptime(month_name, "%b")
    except ValueError:
        month_name = datetime.strptime(month_name, "%B")
    return int(year_name[0]), month_name.month


def give_applicants_unique_id(df, aws_file_name):
    df = df.reset_index()
    df = df.rename(columns={"index": "applicant_id"})
    y, m = convert_month_year_into_id(aws_file_name)

    # set the new index into the new format with 2-digit year,
    # 2-digit month, followed by 4-digit row index
    for i in range(df["applicant_id"].size):
        old_id = df.iloc[i, df.columns.get_loc("applicant_id")]
        new_id = (y % 1000) * 1000000
        new_id += m * 10000
        new_id += old_id
        df.iloc[i, df.columns.get_loc("applicant_id")] = new_id
    return df


def reset_row_ids(df):
    df = df.reset_index()
    df = df.drop(columns="index")
    return df


def save_file(file, filename):
    with open(filename, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_file(filename):
    with open(str(filename), 'rb') as handle:
        b = pickle.load(handle)
    return b


def save_load_file(file, filename):
    ret = 0
    try:
        ret = load_file(filename)
    except FileNotFoundError:
        save_file(file, filename)
        ret = file
    return ret


def save_excel(file, filename):
    file.to_excel(str(str(filename) + ".xlsx"))


