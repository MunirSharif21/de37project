import boto3


def search_list(search):
    s3_resource = boto3.resource("s3")
    bucket_name = 'data-eng-37-final-project'
    bucket = s3_resource.Bucket(bucket_name)
    bucket_resources = bucket.objects.all()

    talent_json = []

    for i in bucket_resources:
        if search in i.key:
            talent_json.append(i.key)

    return talent_json


# MAIN


# print(search_list("Applicant"))

