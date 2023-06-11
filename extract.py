def extract_all(extract_from, extract_to):

    import zipfile
    import os
    from deleter import delete_files_in_folder

    delete_files_in_folder(extract_to)

    script_directory = os.path.dirname(os.path.abspath(__file__)) #Directory of script

    file_names = []

    target_directory = os.path.join(script_directory, extract_from)

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_names.append((os.path.join(root, file)).split("\\")[-1])

    for file_name in file_names:

        zip_file_path = os.path.join(script_directory, (extract_from + "\\" + file_name))
        destination_folder = os.path.join(script_directory, extract_to)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)