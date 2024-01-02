import os
from datetime import datetime  

def process_files():
    current_dir = os.getcwd()
    markdown_files = [file for file in os.listdir(current_dir) if file.endswith(".md")]

    for file_name in markdown_files:
        updated_name = file_name.rsplit(' ', 1)[0]

        try:
            date_obj = datetime.strptime(updated_name, "%Y%m%d")
            new_file_name = date_obj.strftime("%Y-%m-%d") + ".md"

            os.rename(file_name, new_file_name)
            print("Renamed {} to {}".format(file_name, new_file_name))
        except ValueError:
            print("File {} is not in the correct format".format(file_name))
            continue

if __name__ == "__main__":
    process_files()