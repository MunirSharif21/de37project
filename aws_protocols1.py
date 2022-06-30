import boto3
import botocore
import json
import pandas as pd
from tqdm import tqdm
from botocore.exceptions import ClientError

"""
This file has all the functions relating to the retrieval of
AWS data and loading it into the stage 1 format. It also includes a search function.
Cleaning data is done in cleaning stages,
each stage is denoted by _c# where # denotes the stage number
e.g. df_c2 = dataframe cleaned to stage 2
"""

s3_resource = boto3.resource("s3")
s3 = s3_resource
s3_client = boto3.client("s3")


def read_config():
    """
    Try to read the config file and return the bucket name
    If failed, use the default name
    :return bucket_name: String
    """
    try:
        with open("config/config.txt") as f:
            lines = f.readlines()
        line1 = str(lines[0])
        bucket_name_config = line1.replace("bucket_name=", "")
    except FileNotFoundError:
        # set default name of bucket
        bucket_name_config = 'data-eng-37-final-project'
    return bucket_name_config


# read config file

bucket_name = read_config()
bucket = s3_resource.Bucket(bucket_name)


def search_aws_bucket_files(search):
    """
    This function searches the entire bucket and returns all files containing the
    specified search parameter
    :param search:
    :return list of search results:
    """
    bucket_resources = bucket.objects.all()
    search_results = []
    for i in bucket_resources:
        if search in i.key:
            search_results.append(i.key)
    return search_results


def download_raw_aws_file(file_name):
    try:
        raw_data = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    except s3.meta.client.exceptions.NoSuchKey:
        print("\nThis file does not exist in the bucket!\n")
        raise

    return raw_data


def json_download():
    # bucket_name_aws = 'data-eng-37-final-project'
    bucket_aws = s3_resource.Bucket(bucket_name)
    bucket_resources = bucket_aws.objects.all()
    talent_json = []

    for i in bucket_resources:
        if '.json' in i.key:
            talent_json.append(i.key)

    talent_data = []

    for i in tqdm(talent_json):
        talent_data.append(json.loads(s3_resource.Object(bucket_name, i).get()['Body'].read()))

    return talent_data


def cleaning_stage_1(file_name):
    raw_data = download_raw_aws_file(file_name)
    # check file type and apply the correct loading method
    if ".json" in file_name:
        # print(raw_data["Body"].read())
        # df_c1 = json.loads(raw_data["Body"].read())
        df_c1 = json.loads(raw_data["Body"].read())
    elif ".txt" in file_name:
        df_c1 = pd.read_csv(raw_data["Body"], sep="\t", header=None)
    elif ".csv" in file_name:
        df_c1 = pd.read_csv(raw_data["Body"])
    else:
        raise "File Has Wrong Format"
    return df_c1



# MAIN


# print(cleaning_stage_1("Talent/May2019Applicants.csv"))

# print(search_list("Applicant"))
