import pandas as pd
from crawl import activate_crawler
from extract import extract_all
from collate import collate
from merge import merge
from align import align
from csv_names import get_names
from deleter import delete_files_in_folder
from pvmerge import addPV

print("Gathering current data.")

if('database.csv' in get_names("None")):
    main_database = pd.read_csv("database.csv",index_col = [0])
    most_recent_date = (main_database.tail(1)["Unnamed: 0"].to_list()[0]).split(" ")[0] #Finds out how recent my data is.
else:
    most_recent_date = "0000/00/0000"

print("Crawling NEM for new data.")

activate_crawler("raw_zip_files", most_recent_date,'http://www.nemweb.com.au/Reports/ARCHIVE/Dispatch_SCADA/') #Crawls for all the data beyond the most recent date.

print("Extracting daily data.")

extract_all('raw_zip_files', 'next_layer_zip_files') #Extracts the five min interval zip files from the daily zip files.

print("Extracting 5-minutely data.")

extract_all('next_layer_zip_files', 'raw_csv_files') #Extracts the csv files from the 5 min zip files.

print("Collating the data.")

collate() #Collates the 5 min zip files into small (approx daily) csv files.

new_data_file_name = merge("processed_csv_files") #Merges the daily zip files.

new_data = pd.read_csv(new_data_file_name)

print("Searching for rooftop solar data.")

newdata = addPV(new_data)

print("Merging the data with current database.")

if('database.csv' in get_names("None")):
    align(main_database, new_data).to_csv("database.csv")
    delete_files_in_folder("processed_csv_files")
else:
    new_data.to_csv("database.csv")
    delete_files_in_folder("processed_csv_files")

print("You're up to date.")