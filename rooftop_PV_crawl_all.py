from crawl import activate_crawler
from deleter import delete_files_in_folder
from extract import extract_all
from collate import collate_PV

# delete_files_in_folder('rooftop_PV_raw_zip_data')

# activate_crawler("rooftop_PV_raw_zip_data","00/00/0000","http://www.nemweb.com.au/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL/")

# delete_files_in_folder('rooftop_PV_next_layer_zip_data')

# extract_all("rooftop_PV_raw_zip_data","rooftop_PV_next_layer_zip_data")

# delete_files_in_folder('rooftop_PV_raw_csv_data')
# delete_files_in_folder('rooftop_PV_raw_zip_data')

# extract_all("rooftop_PV_next_layer_zip_data","rooftop_PV_raw_csv_data")

# delete_files_in_folder('rooftop_PV_next_layer_zip_data')
# delete_files_in_folder('rooftop_PV_processed_csv_files')
delete_files_in_folder('rooftop_PV_raw_csv_data')
#collate_PV()