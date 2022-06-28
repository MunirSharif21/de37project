from cross_table_utility_functions import *
from combine_table_protocols2 import *


def clean_applicants_table():
    # combine tables
    df_c3 = combine_applicants_tables()
    # split name into new columns and delete the name column
    df_c3 = split_name_into_2(df_c3)
    # clean phone numbers
    df_c3 = apply_to_each_row_in_column(df_c3, "phone_number", clean_phone_numbers)
    # change format of dob
    df_c3 = apply_to_each_row_in_column(df_c3, "dob", change_date_to_ymd)
    # clean the format of "month"
    df_c3 = apply_to_each_row_in_column(df_c3, "month", clean_month_column)
    # clean invited_date
    df_c3 = apply_to_each_row_in_column(df_c3, "invited_date", clean_invited_date)
    # rename column for clarity
    df_c3 = df_c3.rename(columns={"uni": "university"})
    # fix trainer names
    df_c3 = apply_to_each_row_in_column(df_c3, "invited_by", fix_spelling)
    return df_c3


