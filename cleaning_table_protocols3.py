from combine_table_protocols2 import *
from json_txt_cleaning import *
from cross_table_utility_functions import *
from clean_applicants_table import *
from academy_table import *
from cohort_table import *
from course_info_table import *


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
    # fix name capitals
    df_c3 = apply_to_each_row_in_column(df_c3, "last_names", fix_capitals)
    # remove fractions from scores
    df_c3 = apply_to_each_row_in_column(df_c3, "Psychometrics", removeFraction)
    df_c3 = apply_to_each_row_in_column(df_c3, "Presentation", removeFraction)
    # remove the word academy from location
    df_c3 = apply_to_each_row_in_column(df_c3, "Location", removeAcademyWord)
    # fix index
    df_c3 = fix_index(df_c3)
    return df_c3


def clean_json():
    df_c3 = combine_json()
    df_c3 = pd.DataFrame(df_c3)
    # split name
    df_c3 = split_name_into_2(df_c3, "name")
    # fix double slashes
    df_c3 = apply_to_each_row_in_column(df_c3, "date", fix_double_slash)
    # change format of dob
    df_c3 = apply_to_each_row_in_column(df_c3, "date", change_date_to_ymd)
    # add applicant ID
    df_c3 = json_add_applicant_id(df_c3)
    # swap columns
    col_list = list(df_c3)
    col_list[0], col_list[1] = col_list[1], col_list[0]
    return df_c3


def clean_academy(force_refresh):
    if force_refresh:
        print("Writing new file...\ndf_academy")
        df_c3 = main2()
        save_file(df_c3, "df_academy")
    try:
        df_c3 = load_file("df_academy")
    except FileNotFoundError:
        print("Writing new file...\ndf_academy")
        df_c3 = main2()
        save_file(df_c3, "df_academy")
    # clean dates
    df_c3 = apply_to_each_row_in_column(df_c3, "date_on_file", date_dash_removal)
    # split names
    df_c3 = split_name_into_2(df_c3, "name")
    # add applicant ID
    df_c3 = json_add_applicant_id(df_c3, col_name="date_on_file")
    return df_c3


def clean_cohort(force_refresh):
    if force_refresh:
        print("Writing new file...\ndf_cohort")
        df_c3 = cohort_table_function()
        save_file(df_c3, "df_cohort")
    try:
        df_c3 = load_file("df_cohort")
    except FileNotFoundError:
        print("Writing new file...\ndf_cohort")
        df_c3 = main2()
        save_file(df_c3, "df_cohort")
    # clean dates
    df_c3 = apply_to_each_row_in_column(df_c3, "date_on_file", date_dash_removal)
    # split name
    df_c3 = split_name_into_2(df_c3, "Name")
    # add applicant ID
    df_c3 = json_add_applicant_id(df_c3, col_name="date_on_file")
    # clean dates
    df_c3 = apply_to_each_row_in_column(df_c3, "date_on_file", date_dash_removal)
    # remove extra column
    df_c3 = df_c3.drop(columns=["date_on_file", "first_name", "last_names"])
    # remove underscroll
    df_c3 = apply_to_each_row_in_column(df_c3, "cohort_id", remove_underscore)
    return df_c3


def clean_course_info():
    df_c3 = the_actual_course_info_table()
    # change format of ID
    df_c3 = apply_to_each_row_in_column(df_c3, "cohort_id", remove_underscore)
    return df_c3



# print(clean_applicants()[:10])
# print(clean_candidates()[:10])
# print(clean_json()[:10])

