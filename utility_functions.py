import re
from datetime import datetime
import pickle
import os
import logging
import logging.config
from os import path


"""
This file provides functions needed to do specific changes to the frames
due to some weird behaviours by other files
"""


def convert_month_year_into_id(file_name):
    # find the year by getting a list of all consecutive numbers
    # let the first consecutive numbers represent the year
    save_log("convert_month_year_into_id")
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
    save_log("give_applicants_unique_id")
    df = df.reset_index()
    df = df.rename(columns={"index": "applicant_id"})
    y, m = convert_month_year_into_id(aws_file_name)

    # set the new index into the new format with 2-digit year,
    # 2-digit month, followed by 4-digit row index
    exists = {}
    for i in range(df["applicant_id"].size):
        old_id = df.iloc[i, df.columns.get_loc("applicant_id")]
        new_id = (y % 1000) * 1000000
        new_id += m * 10000
        new_id += old_id
        if new_id in exists:
            new_id += 8000
        else:
            exists[new_id] = 1
        df.iloc[i, df.columns.get_loc("applicant_id")] = new_id
    return df


def reset_row_ids(df):
    save_log("reset_row_ids")
    df = df.reset_index()
    df = df.drop(columns="index")
    return df


def save_file(file, filename):
    save_log("save_file")
    with open(filename, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_file(filename):
    save_log("load_file")
    with open(str(filename), 'rb') as handle:
        b = pickle.load(handle)
    return b


def save_load_file(file, filename):
    save_log("save_load_file")
    ret = 0
    try:
        ret = load_file(filename)
    except FileNotFoundError:
        save_file(file, filename)
        ret = file
    return ret


def save_excel(file, filename):
    save_log("save_excel")
    file.to_excel(str(str(filename) + ".xlsx"))


def save_log(text):
    no_logs = True
    if not no_logs:
        try:
            logger = logging.getLogger(__name__)
            logger.debug(text)
            # f = open("logs/logs.txt", "a")
            # time_stamp = datetime.now()
            # now = str(time_stamp.strftime("%d/%m/%Y %H:%M:%S:%f"))
            # now = now[:-2]
            # f.write("\n[" + now + "] " + text)
            # f.close()
        except FileNotFoundError:
            print("No log file found")


def reset_log():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logs/log_config.txt')
    logging.config.fileConfig(log_file_path)
    # logging.config.fileConfig(fname="logs/log_config.txt", disable_existing_loggers=False)
    # Get the logger specified in the file




