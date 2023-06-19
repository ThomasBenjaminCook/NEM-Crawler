def align(database1, database2):
    import pandas as pd

    current_array = database1["Datetime"].to_list()

    target_index = "Null"

    for time in database2["Datetime"]:
        if time not in current_array:
            database1 = pd.concat([database1,database2[database2["Datetime"]==time]]).fillna(0)
            target_index = database2[database2["Datetime"]==time].index.values[0]
            break

    endpoint = (len(database2["Datetime"]))

    if(target_index == 'Null'):
        return(database1)
    else:
        return(pd.concat([database1,database2.iloc[target_index:endpoint,:]]).fillna(0).reset_index(drop=True))