import pandas as pd
from tqdm import tqdm
from aws_protocols1 import *
from clean_functions import *
from utility_functions import *

"""
This file applies combining functions to the tables to produce a single table
Only *essential* cleaning is done, the remainder is done in the cleaning_table_protocols
"""

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
pd.set_option("display.max_rows", 999)


def combine_applicants_tables():
    # get all files
    file_names = search_aws_bucket_files("Applicants")
    list_of_tables = []
    for file in file_names:
        downloaded_table = cleaning_stage_1(file)
        # add applicant IDs
        downloaded_table = give_applicants_unique_id(downloaded_table, file)
        downloaded_table = delete_column(downloaded_table, "id")
        list_of_tables.append(downloaded_table)
    # now combine all the frames
    df_c2 = pd.DataFrame()
    for frame in list_of_tables:
        df_c2 = pd.concat([df_c2, frame], axis=0)
    df_c2 = reset_row_ids(df_c2)
    return df_c2


def combine_json():
    try:
        df_c2 = load_file("json_download")
    except FileNotFoundError:
        print("Writing new file...")
        df_c2 = json_download()
        save_file(df_c2, "json_download")
    return df_c2


# MAIN

# print(combine_json())
