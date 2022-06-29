from aws_protocols1 import *
#print(cleaning_stage_1("Academy/Data_37_2019-11-18.csv"))

def check_course_length(df0):
    """returns the number of weeks of each course as an integer"""
    return int((len(df0.columns)-2)/6)


def weeks_completed(df0):
    """returns dataframe listing each applicant(name - need to change to id)"""
    col2 = []
    for i in range(0, len(df0.index)):
        col2.append(int(check_course_length(df0) - df0.loc[[i]].isna().sum().sum()/6))
    df1 = pd.DataFrame({"Name":df0.iloc[:,0], "weeks_completed" : col2})
    return df1


#print(check_course_length(cleaning_stage_1("Academy/Data_37_2019-11-18.csv")))
#print(weeks_completed(cleaning_stage_1("Academy/Data_37_2019-11-18.csv")))
#print(type(weeks_completed(cleaning_stage_1("Academy/Data_37_2019-11-18.csv"))))
print(cleaning_stage_1("Academy/Data_37_2019-11-18.csv"))
print(cleaning_stage_1("Academy/Data_37_2019-11-18.csv").loc[[0]].isna().sum().sum())
print(weeks_completed(cleaning_stage_1("Academy/Data_37_2019-11-18.csv")))