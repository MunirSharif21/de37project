import boto3
import pandas as pd
import json


def get_file_with_key(url, type_n):
    s3_client = boto3.client("s3")
    bucket_name = "data-eng-37-final-project"
    temp = s3_client.get_object(Bucket=bucket_name, Key=url)
    if type_n == "json":
        temp = json.loads(temp["Body"].read())
    elif type_n == "csv":
        temp = pd.read_csv(temp["Body"])
    return temp



