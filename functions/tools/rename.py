import os


def rename_files(dic_path):
    if " " in dic_path:
        dic_path = dic_path.replace(" ", "_")
    try:
        for counter, filename in enumerate(os.listdir(dic_path)):
            if os.path.isfile(os.path.join(dic_path, filename)):

                file_type = filename.split(".")[-1]
                name = check_filename(dic_path)
                new_name = f"{name}-{counter}{os.path.splitext(dic_path)[1]}.{file_type}"

                # Rename data
                os.rename(os.path.join(dic_path, filename), os.path.join(dic_path, new_name))

            print(counter, filename, dic_path)
        return f"All files in '{dic_path}' were renamed."
    except Exception as e:
        return f"Error {e} while trying to rename files in '{dic_path}'"


def rename_dictionary(path, new_path):
    os.rename(path, os.path.join(os.path.dirname(path), new_path))


def check_filename(dic_path):
    path = dic_path.split("\\")[-1]
    parent_folder = dic_path.split("\\")[-2]
    if path.isnumeric():
        return f"{parent_folder}_{path}"
    else:
        return path
