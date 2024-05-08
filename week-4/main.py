from pathlib import Path
import os

def main():

    root_path = Path("./data")

    if(not root_path.exists()):
        print("Path doesn't exist!")
        raise
    elif(not root_path.is_dir()):
        print("Path isn't a directory")
        raise
    else:
        print("Folder exists")

    root_path.mkdir()



    
    days = [
        "Monday", # 0th
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday" #6th
    ]


    for day in days:
        directory_path = Path(root_path, day)
        print(directory_path)
        directory_path.mkdir()

if __name__ == "__main__":
    main()