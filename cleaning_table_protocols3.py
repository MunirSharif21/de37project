from combine_table_protocols import *

"""
This file contains functions that actually clean the date
Normalisation is NOT performed at all
"""


def clean_applicants():
    # combine tables
    df = combine_applicants_tables()
    # split name into new columns and delete the name column
    df = split_name_into_3(df)
    # clean phone numbers
    df = apply_to_each_row_in_column(df, "phone_number", clean_phone_numbers)
    # change format of dob
    df = apply_to_each_row_in_column(df, "dob", change_date_to_ymd)
    # clean the format of "month"
    df = apply_to_each_row_in_column(df, "month", clean_month_column)
    # clean invited_date
    df = apply_to_each_row_in_column(df, "invited_date", clean_invited_date)
    # rename column for clarity
    df = df.rename(columns={"uni": "university"})
    return df


# print(clean_applicants())
