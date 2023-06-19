def addPV(data_peice_old):   
    import pandas as pd
    from rooftop_PV_crawl_all import crawl_PV

    data_peice = data_peice_old

    stringdate = data_peice["Datetime"].to_numpy()[0]

    firstdate = pd.to_datetime(stringdate, format = "%Y/%m/%d %H:%M:%S")

    pvdata = crawl_PV(stringdate.split(" ")[0])

    numpytimes = pvdata["Time"].to_numpy()
    numpypowers = pvdata["Output"].to_numpy()

    newtimes = []
    newpower = []

    countindex = 0
    for time in numpytimes:
        oldtime = time.split(" ")[-1].split(":")
        minutes = oldtime[1]
        for count in range(0,30,5):
            newactualtime = str(int(minutes)+count)
            if(len(newactualtime) == 1):
                newactualtime = "0" +  newactualtime
        
            newpower.append(numpypowers[countindex])

            oldtime[1] = newactualtime
            outputdatetime = [time.split(" ")[0]]
            outputdatetime.append((":").join(oldtime))
            outputdatetime = (" ").join(outputdatetime)

            newtimes.append(outputdatetime)
        
        countindex += 1 

    expandeddata = pd.DataFrame({"Time":newtimes,"Power":newpower})
    expandeddata["Time"] = pd.to_datetime(expandeddata["Time"],format="%Y/%m/%d %H:%M:%S")
    expandeddata = (expandeddata[expandeddata["Time"] >=firstdate])

    number_to_drop = (len(data_peice.iloc[:,1])-len(expandeddata.iloc[:,1]))

    data_peice.drop(data_peice.tail(number_to_drop).index, inplace = True)

    data_peice["RooftopPV"] = expandeddata['Power'].to_numpy()

    return(data_peice)