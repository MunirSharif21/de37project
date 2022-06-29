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
    df_academy = get_tables_4()
    df_app.to_pickle("tables_pickle_file/applicant_table")
    df_add.to_pickle("tables_pickle_file/address_table")
    df_rec.to_pickle("tables_pickle_file/recruiter_table")
    df_json.to_pickle("tables_pickle_file/interview_table")
    df_scores.to_pickle("tables_pickle_file/tech_scores_table")
    df_lang.to_pickle("tables_pickle_file/languages_table")
    df_candidates.to_pickle("tables_pickle_file/assessment_day_table")
    df_locations.to_pickle("tables_pickle_file/location_table")
    df_stren_names.to_pickle("tables_pickle_file/strength_names")
    df_stren.to_pickle("tables_pickle_file/strengths")
    df_weak.to_pickle("tables_pickle_file/weaknesses")
    df_weak_names.to_pickle("tables_pickle_file/weak_names")
    df_academy.to_pickle("tables_pickle_file/academy")
    # df_behaviours.to_pickle("tables/behaviours")


# save_to_csv()
all_tables = []
# print(pd.read_pickle("tables/tech_scores_table.csv"))
# for i in get_tables_1():
#     all_tables.append(i)
# for i in get_tables_2():
#     all_tables.append(i)
# for i in get_tables_3():
#     all_tables.append(i)
# for i in get_tables_4():
#     all_tables.append(i)

# df_app, df_add, df_rec = get_tables_1()
# df_json, df_scores, df_stren, df_weak = get_tables_2()
# df_candidates, df_locations = get_tables_3()
# df_academy = get_tables_4()
# print(df_academy[:10])


# print(df_app, df_add, df_rec, sep="\n")

# save_excel(df_app, "applicants_table")
# save_excel(df_add, "address_table")
# save_excel(df_rec, "recruiters_table")
# lim = 20
# for i, v in enumerate(all_tables):
#     if i >= lim:
#         break
#     print(v[:20], end="\n\n")

# print(df_academy[:10])
# print(df_behaviours[:10])

