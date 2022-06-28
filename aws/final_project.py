import boto3
from pprint import pprint
import json_cleaning

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'data-eng-37-final-project'
def key_to_dict(the_key):
    s3_object = s3_client.get_object(
        Bucket=bucket_name,
        Key=the_key
    )

    strbody = s3_object['Body'].read()
    return json.loads(strbody)


def get_interview_keys():
    keys = [o.key for o in
            s3_resource.Bucket(bucket_name).objects.all()]  # way to look at all keys (filenames) in 1 line
    filtered_keys = []
    for key in keys:
        if key.split('/')[0] == 'Talent':
            if key.split('.')[-1] == 'json':
                filtered_keys.append(key)
    return filtered_keys


def load_all():
    every_interview = []
    count = 1
    keys = get_interview_keys()
    for key in keys:
        print(f"Loading json data: {count / len(keys) * 100:.2f}%")
        count += 1
        every_interview.append(key_to_dict(key))
    return every_interview


interviews = load_all()
print('All interview data loaded\n')

while True:
    search = input('\nEnter search criteria: ').lower()
    results = []
    for interview in interviews:
        if interview['name'].lower() == search:
            results.append(interview)

    print(f'Results: {len(results)}\n')
    for result in results:
        pprint(result)