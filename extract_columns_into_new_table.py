from cleaning_functions import *
import re
from create_applicant_id import *

##########
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
##########

df4 = get_clean_DF4(k="Talent/May2019Applicants.csv")
# k = "Talent/May2019Applicants.csv"
df2 = get_clean_DF2()


# print(df4)


def extract_remove_columns(df, cols, address=False, deletion=True):
    new_df = df[cols]
    if deletion:
        df = df.drop(columns=cols)
    if address:
        # cols.append("applicant_id")
        new_df = pd.concat([df["applicant_id"], new_df], axis=1)
    return df, new_df


