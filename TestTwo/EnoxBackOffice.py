from importlib import reload
from time import sleep
import requests
import json
import zipfile
import pathlib
import os
import subprocess
# from reloading import reloading


def start():
    subprocess.run(["main/main.exe"])
    path = pathlib.Path("main.zip")
    if pathlib.Path.exists(path):
        try:
            with zipfile.ZipFile("main.zip") as zip:
                # print(zip.getinfo("main/main.exe"))
                zip.extractall()
                print("done extracting")
        except Exception as e:
            print(e)
            print("ett problem har hänt")
        try:
            os.remove("main.zip")
            print("Script reloaded and function executed successfully.")
        except Exception as e:
            print(e)
            print("another problem")
    else:
        print("it doesn't exist")
    print("end\n\n")
    sleep(2)


if __name__ == "__main__":
    module_name = (
        "h"  # Replace with your script's module name (without the .py extension)
    )
    while True:
        print(f"Reloading {module_name}...")
        start()
        sleep(2)
