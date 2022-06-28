import boto3
import pandas as pd
import json

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
pd.set_option('display.max_rows', None)

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data-eng-37-final-project'
bucket = s3_resource.Bucket(bucket_name)
bucket_resources = bucket.objects.all()
talent_json = []

for i in bucket_resources:
    if '.json' in i.key:
        talent_json.append(i.key)

talent_data = []
count = 0
for i in talent_json:
    talent_data.append(json.loads(s3_resource.Object(bucket_name, i).get()['Body'].read()))

df_nested_list = pd.json_normalize(talent_data)
df_nested_list.columns = ["Name", "Date", "Strengths", "Weaknesses", "Location"]

print(type(df_nested_list))
print(df_nested_list)