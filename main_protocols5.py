from pandas import to_pickle
import pickle
from get_table_protocols4 import *


"""
This is the MAIN protocols file that controls everything else
"""


# import subprocess
# import sys
#
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# install(pickle)


def save_to_csv():
    df_app, df_add, df_rec = get_tables_1()
    df_json, df_scores, df_stren, df_weak, df_lang, df_stren_names, df_weak_names = get_tables_2()
    df_candidates, df_locations = get_tables_3()
    df_academy, df_cohort, df_cohort_info = get_tables_4()
    df_app.to_csv("clean_csv/applicant_table.csv")
    df_add.to_csv("clean_csv/address_table.csv")
    df_rec.to_csv("clean_csv/recruiter_table.csv")
    df_json.to_csv("clean_csv/interview_table.csv")
    df_scores.to_csv("clean_csv/tech_scores_table.csv")
    df_lang.to_csv("clean_csv/languages_table.csv")
    df_candidates.to_csv("clean_csv/assessment_day_table.csv")
    df_locations.to_csv("clean_csv/location_table.csv")
    df_stren_names.to_csv("clean_csv/strengths.csv")
    df_stren.to_csv("clean_csv/applicant_strengths.csv")
    df_weak.to_csv("clean_csv/applicant_weaknesses.csv")
    df_weak_names.to_csv("clean_csv/weaknesses.csv")
    df_academy.to_csv("clean_csv/academy.csv")
    df_cohort.to_csv("clean_csv/cohort.csv")
    df_cohort_info.to_csv("clean_csv/course_info.csv")


reset_log()


# save_to_csv()


# print(pd.read_pickle("tables_pickle_file")[:20])


def get_all_tables_list():
    all_tables = []
    for i in tqdm(get_tables_1()):
        all_tables.append(i)
    for i in tqdm(get_tables_2()):
        all_tables.append(i)
    for i in tqdm(get_tables_3()):
        all_tables.append(i)
    for i in tqdm(get_tables_4()):
        all_tables.append(i)
    return all_tables


all_tables = []

for i in tqdm(get_tables_1()):
    all_tables.append(i)
# for j in all_tables:
#     save_excel(j, str(j))
save_excel(all_tables[0], "test11")

# for i in tqdm(get_tables_2()):
#     all_tables.append(i)
# for i in tqdm(get_tables_3()):
#     all_tables.append(i)
# for i in tqdm(get_tables_4()):
#     all_tables.append(i)

# lim = 99
# for i, v in enumerate(all_tables):
#     if i >= lim:
#         break
#     print(v[3590:3600], end="\n\n")
