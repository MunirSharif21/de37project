from combine_applicant_id_tables import *


def create_translator(df0):
    name_id = {}
    for i in range(df0["applicant_id"].size):
        first_name = df0.iloc[i, df0.columns.get_loc("First Name")]
        last_name = df0.iloc[i, df0.columns.get_loc("Last Name")]
        full_name = first_name + " " + last_name
        name_id[full_name] = df0.iloc[i, df0.columns.get_loc("applicant_id")]
    return name_id


name_to_id = create_translator(df)
# print(name_to_id)

