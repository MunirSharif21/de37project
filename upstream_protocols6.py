import os
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine import URL
from main_protocols5 import *

# https://stackoverflow.com/questions/60746034/data-source-name-too-long-error-with-mssqlpyodbc-in-sqlalchemy

my_uid = "admin"
my_pwd = "spartaglobal"
my_host = "database-1.calyepmxm6dy.eu-central-1.rds.amazonaws.com"
my_db = "upstream_test"
my_schema = "final_project_sql_tables.txt"
my_odbc_driver = "ODBC Driver 17 for SQL Server"

connection_uri = URL.create(
    "mssql+pyodbc",
    username=my_uid,
    password=my_pwd,
    host=my_host,
    database=my_db,
    query={"driver": my_odbc_driver},
    )
# print(connection_uri)
engine = sa.create_engine(connection_uri, fast_executemany=True)
# print(engine.table_names())

csv_location = "C:/Users/Konrad/OneDrive/_Sparta/_project/clean_csv"
dir_list = os.listdir(csv_location)


def add_tables_to_sql(tables_list):
    table_names = ["applicant", "address", "recruiter", "athens_day", "scores",
                   "strength", "weakness", "language_name", "strength_name",
                   "weakness_name", "candidates", "academy",
                   "cohort", "cohort_info"]
    # table_names = ["strength_name"]
    for i, v in tqdm(enumerate(table_names)):
        table = tables_list[i]
        table.to_sql(v, engine, if_exists="replace", index=False)
    # for file in dir_list:
    #     # file = "whatever.csv"
    #     csv_name = file.replace('.csv', '')  # remove .csv from string
    #     print(csv_name)
    #     for table in engine.table_names():
    #         if table == csv_name:
    #             df = pd.read_csv(csv_location + file)
    #             # df.to_sql(con=engine, index_label='id')
    #             # now import the data from the csv


# MAIN
force_update = True
if force_update:
    tables = get_all_tables_list()
else:
    try:
        tables = load_file("tables_list")
    except FileNotFoundError:
        tables = get_all_tables_list()
        save_file(tables, "tables_list")
# print(tables[0][:10])
add_tables_to_sql(tables)


