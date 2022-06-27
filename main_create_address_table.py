from extract_columns_into_new_table import *


def extract_address_from_applicants(df44):
    df44, df_address = extract_remove_columns(df44, ["city", "address", "postcode"], address=True)
    # print(df44)
    # print(df_address)
    return df44, df_address

