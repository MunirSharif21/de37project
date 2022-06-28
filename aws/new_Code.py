import boto3  # Needed to access the files in s3
from datetime import datetime
import pandas as pd

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")
bucket_name = "data-eng-37-final-project"
bucket = s3_resource.Bucket(bucket_name)


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
    # print("HELLO\n\n\n")
    for i in range(2, df0.size):
        # print(i, df0.loc)
        x = str(df0.loc[i]).replace("-", ",")
        x = x.replace(":", ",")
        x = x.replace("\nName", " ")
        x2 = x.split(",")
        y0 = x2[0].replace("0", "")
        y0 = y0.strip()
        y1 = x2[2].strip()
        y2 = x2[4].strip()
        temp_list.append([y0, y1, y2, date, location])
    return temp_list


full_table = []
for i in talent_txt:
    test3 = s3_client.get_object(
        Bucket=bucket_name,
        Key=i
        )
    df3 = pd.read_csv(
        test3["Body"], sep="\t",
        header=None)
    y = text_change(df3[:10])
    pd_y = pd.DataFrame(y)
    pd_y.to_csv(sep=",", index=False)
    pd_y.columns = ["Name", "Psychometrics", "Presentation", "Date", "Location"]

    print(pd_y)
