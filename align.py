def align(database1, database2):
    import pandas as pd

    current_array = database1.iloc[:,1].to_list()

    target_index = "Null"

    for time in database2.iloc[:,1]:
        if time not in current_array:
            database1 = pd.concat([database1,database2[database2.iloc[:,1]==time]]).fillna(0)
            target_index = database2[database2.iloc[:,1]==time].index.values[0]
            break

    endpoint = (len(database2.iloc[:,1]))

    if(target_index == 'Null'):
        return(database1)
    else:
        return(pd.concat([database1,database2.iloc[target_index:endpoint,:]]).fillna(0).reset_index(drop=True))