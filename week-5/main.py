from pathlib import Path
import os

def main():

    root_path = Path("./data")


    # if (root_path.exists()):
    #     raise FileExistsError("Path exists!")

    root_path.mkdir(exist_ok=True)

    months = [
        "Jan",
        "Feb",
        "Mar"
    ]

    for month in months:
        month_path = Path(root_path, month)
        month_path.mkdir()
        for day in range(31):
            directory_path = Path(month_path, str(day+1))
            print(directory_path)
            directory_path.mkdir()


if __name__ == "__main__":
    main()