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
    df_app.to_csv("tables2/applicant_table.csv")
    df_add.to_csv("tables2/address_table.csv")
    df_rec.to_csv("tables2/recruiter_table.csv")
    df_json.to_csv("tables2/interview_table.csv")
    df_scores.to_csv("tables2/tech_scores_table.csv")
    df_lang.to_csv("tables2/languages_table.csv")
    df_candidates.to_csv("tables2/assessment_day_table.csv")
    df_locations.to_csv("tables2/location_table.csv")
    df_stren_names.to_csv("tables2/strength_names.csv")
    df_stren.to_csv("tables2/strengths.csv")
    df_weak.to_csv("tables2/weaknesses.csv")
    df_weak_names.to_csv("tables2/weak_names.csv")
    df_academy.to_csv("tables2/academy.csv")
    # df_behaviours.to_pickle("tables/behaviours")


save_to_csv()
all_tables = []
# print(pd.read_pickle("tables_pickle_file")[:20])

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
#
# print(df_academy[:10])
# print(df_behaviours[:10])

