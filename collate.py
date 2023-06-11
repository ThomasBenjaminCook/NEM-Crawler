def collate():
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