import boto3
import pandas as pd
from datetime import datetime
from pprint import pprint

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-37-final-project'

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 800)
pd.set_option('display.max_rows', None)

def text_change(df0):
    temp_list = []
    d = df0.loc[0]
    location = str(df0.loc[1])[2:]
    location = location.strip()
    location = location.replace("\nName: 1, dtype: object", "")
    d = d.replace("\nName: 0,", "")
    dd = str(d).strip()[3:]
    dd = dd.replace("Name: 0, dtype: object", "")
    dd = dd.strip()
    date = datetime.strptime(dd, "%A %d %B %Y")
    date = date.strftime('%Y/%m/%d')
    # print(dd)
    for i in range(2, df0.size):
        # print(df0.loc)
        x = str(df0.loc[i]).replace(" -  ", ",")
        x = x.replace(":", ",")
        x = x.replace("\nName", " ")
        x2 = x.split(",")
        y0 = x2[0].replace("0", "")  # Removing 0's with nothing
        y0 = y0.strip()
        y1 = x2[2].strip()
        y2 = x2[4].strip()
        temp_list.append([y0, y1, y2, date, location])
    return temp_list

# keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]
# print(keys)

bucket = s3_resource.Bucket(bucket_name)
bucket_resources = bucket.objects.all()

talent_txt = []
for i in bucket_resources:
    if '.txt' in i.key:
        talent_txt.append(i.key)

full_df = []
for x in talent_txt:
    test = s3_client.get_object(
        Bucket=bucket_name,
        Key=x
    )
    df = pd.read_csv(test["Body"], sep="\t", header=None)
    df2 = text_change(df)
    df2 = pd.DataFrame(df2)
    df2.to_csv(sep=",", index=False)
    full_df.append(df2)

combined_csv = pd.concat(full_df)
combined_csv.columns = ["Name", "Psychometrics", "Presentation", "Date", "Location"]

pprint(combined_csv)