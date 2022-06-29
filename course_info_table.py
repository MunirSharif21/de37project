import pandas as pd
from aws_protocols1 import *
from cohort_table import *


#files = search_aws_bucket_files("Academy/")
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
    while "Ely Kely" in trainers:
        trainers[trainers.index("Ely Kely")] = "Elly Kelly"
    trainer_ids = list(set(trainers))
    trainer_ids.sort()
    trainer_dict={}
    j = 0
    for name in trainer_ids:
        trainer_dict[name] = j
        j += 1
    df1 = pd.DataFrame({"cohort_id": ids, "stream": streams, "trainer": trainers, "start_date": dates, "weeks": weeks})
    df2 = df1.replace({"trainer": trainer_dict})
    return df2


def the_actual_course_info_table():
    files = search_aws_bucket_files("Academy/")
    return create_course_info(files)

#print(the_actual_course_info_table())

the_actual_course_info_table().to_csv('course_info_table.csv')