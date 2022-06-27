import json
import io
import copy
import io
import pickle

import boto3
from pprint import pprint
from cleaning_functions import *
from tqdm import tqdm


def generate_name_dict():
    s3_client = boto3.client("s3")
    s3_resource = boto3.resource("s3")
    bucket_list = s3_client.list_buckets()
    bucket_name = "data-eng-37-final-project"
    bucket = s3_resource.Bucket(bucket_name)
    bucket_name = "data-eng-37-final-project"

    objects = bucket.objects
    name_list = {}
    for v in tqdm(objects.all()):
        n = v.key
        if "Talent/" in n and "Sparta" not in n and "Applicants" not in n:
            # print(i, v.key, v)
            k = v.key
            # print(i, k)
            test2 = s3_client.get_object(Bucket=bucket_name, Key=k)
            test2 = json.loads(test2["Body"].read())
            name_list[(test2["name"])] = k
    with open('saved_name_list.pkl', 'wb') as f:
        pickle.dump(name_list, f)
    return name_list


def get_name_dict(force_update=False):
    """
    Load the saved
    :param force_update:
    :return:
    """
    if force_update:
        name_list = generate_name_dict()
    else:
        try:
            with open('saved_name_list.pkl', 'rb') as f:
                name_list = pickle.load(f)
        except FileNotFoundError:
            name_list = generate_name_dict()

    return name_list



