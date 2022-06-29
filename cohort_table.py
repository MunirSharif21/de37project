import pandas as pd
from aws_protocols1 import *


#files = search_aws_bucket_files("Academy/")
#files = ["Academy/Data_37_2019-11-18.csv"]

def check_course_length(file_name):
    """returns the number of weeks of each course as an integer"""
    df0 = cleaning_stage_1(file_name)
    return int((len(df0.columns)-2)/6)


def weeks_completed(file_name):
    """returns dataframe listing each applicant(name - need to change to id) with their cohort_id
    and number of weeks they stayed on the course"""
    df0 = cleaning_stage_1(file_name)
    col2 = []
    col3 = []
    col4 = [str(file_name)[-14:-4]] * (len(df0.index))
    for i in range(0, len(df0.index)):
        col2.append(file_name.replace('_', ' ').strip("Academy/")[:-15])
        col3.append(int(check_course_length(file_name) - df0.loc[[i]].isna().sum().sum()/6))
    df1 = pd.DataFrame({"Name":df0.iloc[:,0], "cohort_id": col2, "weeks_completed" : col3, "date_on_file": col4})
    return df1

def joined_cohort_table(file_list):
    joint_df = weeks_completed(file_list[0])
    for i in range(1, len(file_list)):
        joint_df = pd.concat([joint_df, weeks_completed(file_list[i])])
    return joint_df

#print(joined_cohort_table(search_aws_bucket_files("Academy/")))

def cohort_table_function():
    """this just returns the cohort table but names need replacing with applicant_id
     and theres an extra column for the date on the file"""
    big_df = joined_cohort_table(search_aws_bucket_files("Academy/"))
    big_df.index = range(0, len(big_df))
    return big_df

print(cohort_table_function())

