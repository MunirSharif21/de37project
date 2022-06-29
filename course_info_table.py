import pandas as pd
from aws_protocols1 import *
from cohort_table import *


files = search_aws_bucket_files("Academy/")
#files = ["Academy/Data_37_2019-11-18.csv", "Academy/Business_20_2019-02-11.csv"]

def create_course_info(file_list):
    ids = []
    streams = []
    for file_name in file_list:
        ids.append(file_name.strip("Academy/")[:-15])
        streams.append(file_name.strip("Academy/")[:file_name.strip("Academy/").find("_")])
    trainers = []
    dates = []
    weeks = []
    for file_name in file_list:
        df0 = cleaning_stage_1(file_name)
        trainers.append(df0.iloc[1,1])
        dates.append(str(file_name)[-14:-4].replace('-','/'))
        weeks.append(check_course_length(file_name))
    df1 = pd.DataFrame({"cohort_id": ids, "stream": streams, "trainer": trainers, "start_date": dates, "weeks": weeks})
    return df1

print(create_course_info(files))