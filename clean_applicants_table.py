from cross_table_utility_functions import *


def txt_add_applicant_id(df0):
    id_list = []
    mapping = generate_name_date_id_map()
    for row in range(df0["applicant_id"].size):
        f_name = df0.iloc[row, df0.columns.get_loc("first_name")]
        l_name = df0.iloc[row, df0.columns.get_loc("last_names")]
        print(f_name, l_name)



