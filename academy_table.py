from aws_protocols1 import *

# this is probably very inefficient

files = search_aws_bucket_files("Academy/")
# files = ["Academy/Data_37_2019-11-18.csv"]


def unpivot_person(file_name, n):
    """this function takes a file and an integer n to index a person within the file, then returns
    their academy scores in long format"""
    df0 = cleaning_stage_1(file_name)
    df0 = df0.drop(columns=['trainer'])
    column_names = df0.columns[1:]
    weeks = column_names.map(lambda x: int(x[x.find("W")+1:]))
    behaviours = column_names.map(lambda x: x[:x.find("_")])
    trainees = []
    dates = [str(file_name)[-14:-4]] * (len(df0.columns)-1)
    for i in range(0, len(df0.columns)-1):
        trainees.append(df0.iloc[n, 0])
        #dates.append(str(file_name)[-14:-4])
    scores = df0.drop(columns=['name']).loc[n]
    df1 = pd.DataFrame({"name": trainees, "week_number": weeks, "behaviour": behaviours, "score": scores, "date_on_file": dates})
    df2 = df1.dropna()
    df3 = df2.assign(score=df2.score.map(lambda x: int(x)))
    return df3


def unpivot_group(file_name):
    """this function takes a file e.g. 'Academy/Data_37_2019-11-18.csv' and returns the weekly academy
    behaviour scores of a group in long format"""
    df0 = cleaning_stage_1(file_name)
    joint_df = unpivot_person(file_name, 0)
    for i in range(1, len(df0)):
        joint_df = pd.concat([joint_df, unpivot_person(file_name, i)])
    return joint_df


def union_groups(file_list):
    """this function takes a list of academy files e.g. 'Academy/Data_37_2019-11-18.csv' and
    returns them in one dataframe in long format (ERD)"""
    joint_df = unpivot_group(file_list[0])
    for i in range(1, len(file_list)):
        joint_df = pd.concat([joint_df, unpivot_group(file_list[i])])
    return joint_df

# person_1 = unpivot_person(files[0], 0)
# person_1.index=range(0,len(person_1))
# print(person_1)
# print(unpivot_group(files[0]))



# this will print the academy tables (need to replace name with applicant id) with an extra column for the
# dates named on each file to match applicants

all_files = union_groups(files)
all_files.index=range(0,len(all_files))
print(all_files)



