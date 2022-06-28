from clean_functions import *
from utility_functions import *
# from cleaning_table_protocols3 import clean_applicants
from clean_applicants_table import *

"""
This file matches the applicant ID from the applicants table to other files
"""


def generate_name_date_id_map():
    df = clean_applicants_table()
    name_date_id = {}
    # if month < 10:
    #     month_padding = "0" + str(month)
    # else:
    #     month_padding = str(month)
    # year_month = str(month_padding) + "/" + str(year)

    for row in range(df["applicant_id"].size):
        f_name = df.iloc[row, df.columns.get_loc("first_name")].lower()
        l_name = df.iloc[row, df.columns.get_loc("last_names")].lower()
        d_name = df.iloc[row, df.columns.get_loc("month")]
        key = str(f_name) + str(l_name) + str(d_name)
        app_id = df.iloc[row, df.columns.get_loc("applicant_id")]
        name_date_id[key] = app_id

    return name_date_id


def json_add_applicant_id(df0):
    id_list = []
    mapping = generate_name_date_id_map()
    for row in range(df0["applicant_id"].size):
        f_name = df0.iloc[row, df0.columns.get_loc("first_name")]
        l_name = df0.iloc[row, df0.columns.get_loc("last_names")]

        old_date = df0.iloc[row, df0.columns.get_loc("date")]
        temp_date = datetime.strptime(old_date, "%d/%m/%Y")
        new_date = temp_date.strftime("%m/%Y")

        key = str(f_name).lower() + str(l_name).lower() + str(new_date)
        id_value = mapping[key]
        id_list.append(id_value)
    df0.insert(1, "applicant_id", id_list)
    return df0


def txt_add_applicant_id(df0):
    id_list = []
    mapping = generate_name_date_id_map()
    # print(df0)
    for row in range(df0["Name"].size):
        name = df0.iloc[row, df0.columns.get_loc("Name")].lower()
        name = name.replace(" ", "")
        n_date = str(df0.iloc[row, df0.columns.get_loc("Date")])
        n_date = n_date[:7]

        temp_date = datetime.strptime(n_date, "%Y/%m")
        new_date = temp_date.strftime("%m/%Y")
        key = name + str(new_date)
        # print(key, mapping[key])
        id_list.append(mapping[key])
    df0.insert(0, "applicant_id", id_list)
    return df0


# MAIN

# HILARY WILLMORE
# 2019/08/01

# a = generate_name_date_id_map()
# df = pd.DataFrame()
# b = pd.DataFrame.from_dict(a, orient="index")
# print(a["HilaryWillmore08/2019"])
# print(b)
# b = b.reset_index()
# c = b["index"]
# print(c)



