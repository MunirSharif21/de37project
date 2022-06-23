import pandas as pd


def text_change(df0):
    temp_list = []
    for i in range(2, df0.size):
        # print(i, df0.loc)
        x = str(df0.loc[i]).replace("-", ",")
        x = x.replace(":", ",")
        x = x.replace("\nName", " ")
        x2 = x.split(",")
        y0 = x2[0].replace("0", "")
        y0 = y0.strip()
        y1 = x2[2].strip()
        y2 = x2[4].strip()

        temp_list.append([y0, y1, y2])
    return temp_list


def text_change_academy(df0):
    x = []
    for i in df0.keys():
        if type(df0[i]) != dict:
            x.append([i, df0[i]])
        else:
            for j in df0[i].keys():
                x.append([j, df0[i][j]])
    ret = pd.DataFrame(x)
    return ret


def set_first_row_as_column_names(df0):
    df0 = df0.T
    df00 = (df0.iloc[:, :])
    df00.columns = (df0.iloc[0, :])
    df00 = df00.iloc[1, :]
    return df00
