import boto3
from pprint import pprint
import pandas as pd

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data-eng-37-final-project'
def get_applicant_keys():  # gets the keys as a list of strings for all .csv files in the Talent/ folder
    keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]

    filtered_keys = []
    for key in keys:
        if key.split('/')[0] == 'Talent':
            if key.split('.')[-1] == 'csv':
                filtered_keys.append(key)
    return filtered_keys


def convert_date(the_df):
    the_df['invited_date'] = the_df['invited_date'].fillna(-1)
    the_df['invited_date'] = the_df['invited_date'].astype('int').astype('str')
    the_df['converted_date'] = pd.to_datetime(the_df['invited_date'] + the_df['month'])
    return the_df.drop(['invited_date', 'month'], axis=1)

def convert_degree_class(the)

keys = get_applicant_keys()

for key in keys:

    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=key
    )
    file_name = key.split('/')[1]

    this_df = convert_date(pd.read_csv(s3_object['Body']))
    this_df.to_csv(f'applicant/{file_name}', index=False)
    print(f'Converted file: {file_name}')
print("All .csv applicant files converted")


