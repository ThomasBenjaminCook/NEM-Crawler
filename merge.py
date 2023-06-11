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