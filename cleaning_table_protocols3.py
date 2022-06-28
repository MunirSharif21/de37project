from combine_table_protocols2 import *
from elios_file import *
from cross_table_utility_functions import *
from clean_applicants_table import *

"""
This file contains functions that actually clean the date
Normalisation is NOT performed at all
"""


def clean_applicants():
    df_c3 = clean_applicants_table()
    return df_c3


def clean_candidates():
    try:
        df_c3 = load_file("df_c3")
    except FileNotFoundError:
        print("Writing new file...")
        df_c3 = main1()
        save_file(df_c3, "df_c3")
    # add applicant ID
    df_c3 = txt_add_applicant_id(df_c3)
    # split name
    df_c3 = split_name_into_2(df_c3, "Name")
    # remove fractions from scores
    df_c3 = apply_to_each_row_in_column(df_c3, "Psychometrics", removeFraction)
    df_c3 = apply_to_each_row_in_column(df_c3, "Presentation", removeFraction)
    # remove the word academy from location
    df_c3 = apply_to_each_row_in_column(df_c3, "Location", removeAcademyWord)
    # fix index
    df_c3 = fix_index(df_c3)
    return df_c3


# print(clean_applicants())
print(clean_candidates())

