import io

import boto3
from pprint import pprint

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# bucket_list = s3_client.list_buckets()
# # pprint(bucket_list, sort_dicts=False)
#
# for bucket in bucket_list['Buckets']:
#     print(bucket['Name'])

bucket_name = 'data-eng-37-final-project'
# paginator = s3_client.get_paginator('list_objects_v2')
# bucket_contents = paginator.paginate(Bucket=bucket_name)
#
# pprint(bucket_contents, sort_dicts=False)
# for bucket in bucket_contents:
#     for b in bucket['Contents']:
#         print(b['Key'])

bucket = s3_resource.Bucket(bucket_name)
# print(bucket)

objects = bucket.objects
# print(objects)
# print(objects.all())

for object in objects.all():
    print(object.key)
#
# # keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]
# # print(keys)
# #
# # s3_object = s3_client.get_object(
# #     Bucket=bucket_name,
# #     Key='python/chatbot-intent.json'
# # )
# # pprint(s3_object, sort_dicts=False)
# #
# # strbody = s3_object['Body'].read()
# # print(strbody)
# # print(type(strbody))
# #
# import json
# #
# # body = json.loads(strbody)
# # print(body)
#
# # Load python/happiness-2019.csv into a usable form
#
# # s3_object = s3_client.get_object(
# #     Bucket=bucket_name,
# #     Key='python/happiness-2019.csv'
# # )
# #
# #
# import pandas as pd
# #
# # df = pd.read_csv(s3_object['Body'])
# #
# # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
# #     print(df)
#
# # WRITING OBJECTS
#
# dict_to_upload = {'name': 'data', 'status': 1}
#
# with open('abhi.json', 'w') as jsonfile:
#     json.dump(dict_to_upload, jsonfile)
#
# s3_client.upload_file(
#     Filename='abhi.json',
#     Bucket=bucket_name,
#     Key='DE37/abhi.json'
# )
#
# s3_client.put_file(
#     Body=json.dumps(dict_to_upload),
#     Bucket=bucket_name,
#     Key='DE37/abhi.json'
# )
#
# keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]
# print(keys)
#
# import io
#
# df = pd.DataFrame([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
#
# str_buffer = io.StringIO()
# df.to_csv(str_buffer)
# s3_resource.Object(bucket_name, 'DE37/abhi.csv').put(Body=str_buffer.getvalue())
#
