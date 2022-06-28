from get_table_protocols4 import *


"""
This is the MAIN protocols file that controls everything else
"""


df_app, df_add, df_rec = get_tables_1()
df_json, df_scores, df_stren, df_weak = get_tables_2()
df_candidates, df_locations = get_tables_3()

# print(df_app, df_add, df_rec, sep="\n")

# save_excel(df_app, "applicants_table")
# save_excel(df_add, "address_table")
# save_excel(df_rec, "recruiters_table")



# print(b)


