from cleaning_functions import *

##########
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
##########

df4 = get_DF4()
# print(df4)


def extract_remove_columns(df, cols):
    # df = df.reset_index()
    new_df = df[cols]
    df = df.drop(columns=cols)
    return df, new_df


# MAIN

print(df4)
df4, new_df4 = extract_remove_columns(df4, ["city", "address", "postcode"])
print(df4)
print(new_df4)
