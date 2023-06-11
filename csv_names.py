def get_names(target_folder):
    import os
    import pandas as pd

    script_directory = os.path.dirname(os.path.abspath(__file__)) #Directory of script

    file_names = []

    if(target_folder != "None"):
        target_directory = os.path.join(script_directory, target_folder)
    else:
        target_directory = script_directory

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_names.append((os.path.join(root, file)).split("\\")[-1])
    
    return(file_names)