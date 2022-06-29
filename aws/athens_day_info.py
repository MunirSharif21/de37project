import boto3
from datetime import datetime
import pandas as pd


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
    # print("HELLO\n\n\n")
    for i in range(2, df0.size):
        # print(i, df0.loc)
        x = str(df0.loc[i]).replace(" -  ", ",")
        x = x.replace(":", ",")
        x = x.replace("\nName", " ")
        x2 = x.split(",")
        # y0 = x2[0].replace("0", "")  # Removes zeros
        # y0 = y0.strip()
        y1 = x2[2].strip()
        y2 = x2[4].strip()
        temp_list.append([y1, y2, location, date])
    return temp_list

def athens_day_info_normalisation():  # gets the keys as a list of strings for all .csv files in the Talent/ folder
    keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]

    filtered_keys = []
    for key in keys:
        if key.split('/')[0] == 'Talent':
            if key.split('.')[-1] == 'txt':
                filtered_keys.append(key)

    full_table = []
    for k in filtered_keys:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=k
        )
        df3 = pd.read_csv(
            s3_object["Body"], sep="\t",
            header=None)
        y = text_change(df3[:70])
        pd_y = pd.DataFrame(y)
        pd_y.to_csv(sep=",", index=False)
        full_table.append(pd_y)

    combined_df = pd.concat(full_table).reset_index()

    combined_df.columns = ["Name", "Psychometrics", "Presentation", "Location", "Date"]

    df_new2 = combined_df.iloc[:, [3, 4]].drop_duplicates().sort_values("Date").reset_index().drop('index', axis=1)

    df_new = df_new2.rename(columns={'Location': 'academy_name', 'Date': 'date'})

    df_new.index.name = 'academy_day_id'

    csv_new = df_new.to_csv('athens_day_info.csv')

    return csv_new


print(athens_day_info_normalisation())


