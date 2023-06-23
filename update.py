import pandas as pd
from crawl import activate_crawler
from collate import reduce, merge, align
from csv_names import get_names
from deleter import delete_files_in_folder
from pvmerge import addPV
from zip_actions import compress, extract_all

if('database_zip.zip' in get_names("zip_output")):
    extract_all("zip_output","csv_output")
    main_database = pd.read_csv("csv_output/database.csv")
    most_recent_date = (main_database.tail(1)["Datetime"].to_list()[0]).split(" ")[0] #Finds out how recent my data is.
else:
    most_recent_date = "0000/00/0000"

activate_crawler("raw_zip_files", most_recent_date,'http://www.nemweb.com.au/Reports/ARCHIVE/Dispatch_SCADA/') #Crawls for all the data beyond the most recent date.

extract_all('raw_zip_files', 'next_layer_zip_files') #Extracts the five min interval zip files from the daily zip files.

extract_all('next_layer_zip_files', 'raw_csv_files') #Extracts the csv files from the 5 min zip files.

reduce() #Collates the 5 min zip files into small (approx daily) csv files.

new_data_file_name = merge("processed_csv_files") #Merges the daily zip files.

new_data = pd.read_csv(new_data_file_name).rename({"Unnamed: 0":"Datetime"}, axis=1)

newdata = addPV(new_data)

if('database.csv' in get_names("csv_output")):
    align(main_database, new_data).to_csv("csv_output/database.csv", index=False)
    delete_files_in_folder("processed_csv_files")
    compress("database.csv","database_zip.zip")
    delete_files_in_folder("csv_output")
else:
    new_data.to_csv("csv_output/database.csv", index=False)
    delete_files_in_folder("processed_csv_files")
    compress("database.csv","database_zip.zip")
    delete_files_in_folder("csv_output")