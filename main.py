import json
import io
import copy
import io
import boto3
from pprint import pprint
from cleaning_functions import *


s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

bucket_list = s3_client.list_buckets()

bucket_name = 'data-eng-resources'

s3_object = s3_client.get_object(Bucket=bucket_name, Key="python/happiness-2019.csv")

bucket_name = "data-eng-37-final-project"

bucket = s3_resource.Bucket(bucket_name)

#############
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)

test1 = s3_client.get_object(Bucket=bucket_name, Key="Academy/Business_20_2019-02-11.csv")
test2 = s3_client.get_object(Bucket=bucket_name, Key="Talent/13247.json")
test3 = s3_client.get_object(Bucket=bucket_name, Key="Talent/Sparta Day 1 August 2019.txt")
test4 = s3_client.get_object(Bucket=bucket_name, Key="Talent/May2019Applicants.csv")

df = pd.read_csv(test1["Body"])
df2 = json.loads(test2["Body"].read())
df3 = pd.read_csv(test3["Body"], sep="\t", header=None)
df4 = pd.read_csv(test4["Body"])

y = text_change(df3[:10])

pd_y = pd.DataFrame(y)
pd_y.to_csv(sep=",", index=False)
pd_y.columns = ["Name", "Psychometrics", "Presentation"]

print("This is the TALENT/Sparta Day data")
print(df3[:10])
print("\nAFTER CLEANING")
print(pd_y)


print("This is the TALENT/123456 data")
print(df2)
print("\nAFTER CLEANING")
df2_c = text_change_academy(df2)
df2_c = set_first_row_as_column_names(df2_c)
print(df2_c)



