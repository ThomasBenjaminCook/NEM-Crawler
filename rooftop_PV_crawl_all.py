def crawl_PV(time):
    from crawl import activate_crawler
    from deleter import delete_files_in_folder
    from zip_actions import extract_all
    from collate import collate_PV

    delete_files_in_folder('rooftop_PV_raw_zip_data')

    activate_crawler("rooftop_PV_raw_zip_data",time,"http://www.nemweb.com.au/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL/")

    delete_files_in_folder('rooftop_PV_next_layer_zip_data')

    extract_all("rooftop_PV_raw_zip_data","rooftop_PV_next_layer_zip_data")

    delete_files_in_folder('rooftop_PV_raw_csv_data')
    delete_files_in_folder('rooftop_PV_raw_zip_data')

    extract_all("rooftop_PV_next_layer_zip_data","rooftop_PV_raw_csv_data")

    delete_files_in_folder('rooftop_PV_next_layer_zip_data')

    PVdata = collate_PV()

    delete_files_in_folder('rooftop_PV_raw_csv_data')

    return(PVdata)