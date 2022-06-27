from create_applicant_id import *
from search_for_list_of_files import *
from main_create_address_table import *

# df4 = get_clean_DF4(k="Talent/May2019Applicants.csv")
# k = "Talent/May2019Applicants.csv"


pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
pd.set_option("display.max_rows", 999)


def create_combined_list():
    names = search_list("Applicants")
    df_list = []
    for i in names:
        # print(i)
        stage1 = get_clean_DF4(k=i)
        stage2 = insert_base_id(stage1, i)
        df_list.append(stage2)
    return df_list


def fuse_lists_together():
    frames = create_combined_list()
    df0 = pd.DataFrame()
    for i in frames:
        df0 = pd.concat([df0, i], axis=0)
    df0 = df0.reset_index()
    df0 = df0.drop(columns="index")
    return df0


# MAIN


df = fuse_lists_together()

df, df_a = extract_address_from_applicants(df)

print(df)
df.to_excel("applicants_table.xlsx")
df_a.to_excel("address_table.xlsx")

