from get_table_protocols4 import *


"""
This is the MAIN protocols file that controls everything else
"""


def save_to_csv():
    df_app, df_add, df_rec = get_tables_1()
    df_json, df_scores, df_stren, df_weak, df_lang, df_stren_names, df_weak_names = get_tables_2()
    df_candidates, df_locations = get_tables_3()
    df_app.to_csv("tables/applicant_table.csv")
    df_add.to_csv("tables/address_table.csv")
    df_rec.to_csv("tables/recruiter_table.csv")
    df_json.to_csv("tables/interview_table.csv")
    df_scores.to_csv("tables/tech_scores_table.csv")
    df_lang.to_csv("tables/languages_table.csv")
    df_candidates.to_csv("tables/assessment_day_table.csv")
    df_locations.to_csv("tables/location_table.csv")
    df_stren_names.to_csv("tables/strength_names.csv")
    df_weak_names.to_csv("tables/weak_names.csv")


save_to_csv()
all_tables = []
# for i in get_tables_1():
#     all_tables.append(i)
for i in get_tables_2():
    all_tables.append(i)
# for i in get_tables_3():
#     all_tables.append(i)

# print(df_app, df_add, df_rec, sep="\n")

# save_excel(df_app, "applicants_table")
# save_excel(df_add, "address_table")
# save_excel(df_rec, "recruiters_table")


lim = 0
for i, v in enumerate(all_tables):
    if i >= lim:
        break
    print(v[:10], end="\n\n")


