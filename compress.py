def csv_to_zip(csv_name,zip_name):
    from zipfile import ZipFile, ZIP_DEFLATED
    import os

    script_directory = os.path.dirname(os.path.abspath(__file__))
    zip_directory = os.path.join(script_directory, "zip_output")
    zip_location = os.path.join(zip_directory, zip_name)

    csv_directory = os.path.join(script_directory, "csv_output")
    csv_location = os.path.join(csv_directory, csv_name)

    with ZipFile(zip_location, 'w', ZIP_DEFLATED) as zip_object:
        zip_object.write(csv_location,csv_name)