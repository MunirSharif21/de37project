import copy

import pandas as pd
from datetime import datetime
from get_all_names import *
from get_file_with_key import *
import boto3

bucket_name = "data-eng-37-final-project"
s3_client = boto3.client("s3")


def text_change(df0):
    """
    Take a txt file with a specific format:
    Line 1 = Date in the format: "0  Monday 2 January 2023"
    Line 2 = Location name in format: "1  London Academy"
    Line 3 onwards: "firstname lastname - asdf: 99/100, asdf: 31/32", where asdf is ignored
    This is then converted into a list containing smaller lists in the format: [fullname, score1, score2, date, location]
    :rtype: list
    """
    temp_list = []
    d = df0.loc[0]
    location = str(df0.loc[1])[2:]
    location = location.strip()
    location = location.replace("\nName: 1, dtype: object", "")
    d = d.replace("\nName: 0,", "")
    dd = str(d).strip()[3:]
    dd = dd.replace("Name: 0, dtype: object", "")
    dd = dd.strip()
    date = datetime.strptime(dd, "%A %d %B %Y")
    date = date.strftime('%Y/%m/%d')

    for i in range(2, df0.size):
        x = str(df0.loc[i]).replace("-", ",")
        x = x.replace(":", ",")
        x = x.replace("\nName", " ")
        x2 = x.split(",")
        y0 = x2[0].replace("0", "")
        y0 = y0.strip()
        y1 = x2[2].strip()
        y2 = x2[4].strip()
        temp_list.append([y0, y1, y2, date, location])
    return temp_list


def text_change_academy(df0):
    x = []
    lim = 0
    lim1 = 0
    ret1 = []
    ret2 = []
    ret3 = []
    for i in df0.keys():
        if i == "name":
            x_split = df0[i].split(" ")
            x.append(["First Name", x_split[0]])
            x.append(["Last Name", x_split[1]])
            continue
        if type(df0[i]) != dict and type(df0[i]) != list:
            x.append([i, df0[i]])
        # elif type(df0[i]) == list:
        #     if lim == 0:
        #         x.append(["strengths", "Table_Bada_ID"])
        #         ret2 = make_another_table(df0[i], "Strengths")
        #         lim += 1
        #     else:
        #         x.append(["weaknesses", "Table_Chhota_ID"])
        #         ret3 = make_another_table(df0[i], "Weaknesses")
        else:
            if lim1 == 0:
                lim1 += 1
                for j in df0[i].keys():
                    # x.append([j, df0[i][j]])
                    x.append(["Coding_scores", "Table_Some_ID"])
                    ret1 = make_another_table(df0[i], "Scores")
                    break
    # change date format
    x[2][1] = datetime.strptime(x[2][1], "%d/%m/%Y")
    x[2][1] = x[2][1].strftime("%Y/%m/%d")
    # print(x)
    ret = pd.DataFrame(x)
    return ret, ret1, ret2, ret3


def make_another_table(d, n):
    ret = pd.DataFrame({n: d})
    return ret


def set_first_row_as_column_names(df0):
    df0 = df0.T
    df00 = (df0.iloc[:, :])
    df00.columns = (df0.iloc[0, :])
    df00 = df00.iloc[1, :]
    return df00


def clean_single_phone_num(num):
    num = str(num)
    num = num.replace("(", "")
    num = num.replace(")", "")
    num = num.replace("+", "")
    num = num.replace(" ", "")
    num = num.replace("-", "")
    return num


def clean_phone_numbers(nums):
    for i, v in enumerate(nums):
        nums[i] = clean_single_phone_num(v)
    return nums


def dataframe_numbers_cleaning(df):
    for i in range(1, df["phone_number"].size):
        try:
            df.iloc[i - 1, df.columns.get_loc('phone_number')] = clean_single_phone_num(df.iloc[i - 1, df.columns.get_loc('phone_number')])
        except IndexError:
            print(i)
    return df


def split_name(df, col_name = "name"):
    first_names = []
    last_names = []
    for i in range(0, df[col_name].size):
        try:
            full_name = df.iloc[i, df.columns.get_loc(col_name)]
            # print(full_name)
            name_split = full_name.split()
            # print(name_split)
            first_names.append(name_split[0])
            last_names.append(name_split[1])
        except IndexError:
            print(i)
    df.insert(1, "First Name", first_names)
    df.insert(2, "Last Name", last_names)
    # print(first_names)
    # print(last_names)
    df = df.drop(columns=col_name)
    return df


def remove_excess_index(df, index_name):
    df = df.drop(columns=index_name)
    return df


def get_clean_DF4(k="Talent/May2019Applicants.csv"):

    test4 = s3_client.get_object(Bucket=bucket_name, Key=k)
    df4 = pd.read_csv(test4["Body"])
    df4 = dataframe_numbers_cleaning(df4)
    df4 = split_name(df4)
    df4 = remove_excess_index(df4, "id")
    return df4


def get_clean_DF2():
    test2 = s3_client.get_object(Bucket=bucket_name, Key="Talent/13247.json")
    df2 = json.loads(test2["Body"].read())
    df2_c, r2, r3, r4 = text_change_academy(df2)
    df2_c = set_first_row_as_column_names(df2_c)
    df2_c = df2_c.to_frame().T
    return df2_c


def get_clean_DF3():
    test3 = s3_client.get_object(Bucket=bucket_name, Key="Talent/Sparta Day 1 August 2019.txt")
    df3 = pd.read_csv(test3["Body"], sep="\t", header=None)
    y = text_change(df3[:10])

    pd_y = pd.DataFrame(y)
    pd_y.to_csv(sep=",", index=False)
    pd_y.columns = ["Name", "Psychometrics", "Presentation", "Date", "Location"]

    return pd_y


# def combine_rows(key_list):
#     for i, v in tqdm(enumerate(key_list.values())):
#         df22 = get_file_with_key(v, "json")
#         if i == 0:
#             df2_c, r2, r3, r4 = text_change_academy(df22)
#             df2_c = set_first_row_as_column_names(df2_c)
#             df2_c = df2_c.T
#         if i + 10 > 2:
#             break
#
#         print(v)
#         df2_c2, r2, r3, r4 = text_change_academy(df22)
#         df2_c2 = set_first_row_as_column_names(df2_c2)
#         df2_c2 = df2_c2.T
#         df2_c2_2 = copy.deepcopy(df2_c)
#         df2_c2_2 = pd.concat([df2_c2_2, df2_c2], axis=1)
#         # df2_c2_2 = copy.deepcopy(df2_c2_2)
#         # print(df2_c2)
#
#     # df_c2_2 = pd.concat([df2_c, df2_c2], axis=1)
#
#     df2_c2_2 = df2_c2.T
#     return df2_c2_2
#
# print(combine_rows(get_name_dict()))

# nums = ["+44-153-854-3243", "+44 (585) 518-2123"]

# print(clean_phone_numbers(nums))
