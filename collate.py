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

def merge(target_folder):
    import pandas as pd
    from csv_names import get_names
    from deleter import delete_files_in_folder

    file_names = get_names(target_folder)

    new_file_name = target_folder+"/"+file_names[0].split(".")[0] + "to" + file_names[-1].split(".")[0]+".csv"

    father_figure = []
    for file_name in file_names:
        father_figure.append(pd.read_csv(target_folder+"/"+file_name))

    final_result = pd.concat(father_figure).fillna(0)

    delete_files_in_folder(target_folder)

    final_result.to_csv(new_file_name)
    return(new_file_name)

def reduce():
    import pandas as pd
    import numpy as np
    from csv_names import get_names
    from deleter import delete_files_in_folder
    import warnings
    warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

    delete_files_in_folder("processed_csv_files")

    file_names = get_names("raw_csv_files")

    datetimes = []
    stations = []

    count = 0 

    data_frame = pd.DataFrame()

    for file_name in file_names:

        data = pd.read_csv("raw_csv_files/" + file_name)

        outputs = data.iloc[:,6].to_list()[1:-1]
        these_stations = data.iloc[:,5].to_list()[1:-1]

        for station in these_stations:
            if station not in stations:
                data_frame[station] = np.zeros(len(datetimes))
                stations.append(station)

        datetime = (data.iloc[:,4].to_list()[2])
        data_frame.loc[datetime] = np.zeros(len(stations))

        index = 0
        for station2 in these_stations:
            data_frame.loc[datetime,station2]=outputs[index]
            index = index + 1

        datetimes.append(datetime)

        count = count + 1
        if(count > 300):
            count = 0
            datetime_name = ("v").join((datetime.split(" ")[0]).split("/"))
            data_frame.to_csv("processed_csv_files/"+datetime_name+".csv")
            data_frame = pd.DataFrame()
            datetimes = []
            stations = []

    delete_files_in_folder("raw_csv_files")

def collate_PV():
    import pandas as pd
    import numpy as np
    from csv_names import get_names
    from deleter import delete_files_in_folder
    import warnings
    warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
    
    file_names_with_sat = get_names("rooftop_PV_raw_csv_data")

    file_names = []

    for name in file_names_with_sat:
        if(name.split("_")[4] == "MEASUREMENT"):
            file_names.append(name)

    datetimes = []
    output = []

    for file_name in file_names:

        data = pd.read_csv("rooftop_PV_raw_csv_data/" + file_name)
        
        datetimes.append(data["PUBLIC"].loc[1])

        values = (data[data.columns[6]].to_numpy())
        values = (values[1:len(values)-1])

        output.append(values.astype(float).sum())

    dataframe = pd.DataFrame({"Time": datetimes, "Output": output})
    return(dataframe.drop_duplicates(subset=["Time"]))