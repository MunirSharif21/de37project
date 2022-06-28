from cleaning_table_protocols3 import *
from normalisation_functions import *

"""
This file takes a clean table and hence applies normalisation
to it
"""


def applicants_address():
    df_app0 = clean_applicants()
    # extract address into a new table and attach applicant id to it
    df_app0, df_add0 = normalise(df_app0, ["city", "address", "postcode"],
                                 deletion=True, old_id=True, index="applicant_id")
    return df_app0, df_add0


def applicants_recruiter(df_app0):
    # extract recruiters into a new normalised table
    df_app0, df_rec0 = normalise(df_app0, ["invited_by"], deletion=False,
                                 new_id=True, index="invited_by")
    return df_app0, df_rec0


def get_tables():
    df_app, df_add = applicants_address()
    df_app, df_rec = applicants_recruiter(df_app)
    print(df_app, df_rec, sep="\n")
    return df_app, df_add, df_rec


# MAIN



