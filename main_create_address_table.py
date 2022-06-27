from extract_columns_into_new_table import *

df4 = insert_base_id(df4, k)
df4, df_address = extract_remove_columns(df4, ["city", "address", "postcode"], address=True)
print(df4)
print(df_address)

