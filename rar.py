from importlib import reload
from time import sleep
import requests
import json
import zipfile
import pathlib
import os
# from reloading import reloading


def start():
    update = True
    while update:
        version = json.load(open("version.json"))["version"]
        req = requests.post("http://127.0.0.1:8000")
        req_ver = json.loads(req.text)["pk"]
        print("__________________Start__________________")
        print("the version in the cloud:     " + str(req_ver))
        print("Is there any newer version:?  " + str(req_ver > version))
        print("installed version:            " + str(version))
        print("__________________________Latest______________________________")
        print("__________________________Latest______________________________")
        print("__________________________Latest______________________________")
        print("__________________End____________________\n\n")
        path=pathlib.Path('main.zip')
        if(pathlib.Path.exists(path)):
            try:
                with zipfile.ZipFile("main.zip") as zip:
                    zip.extractall()
                os.remove("main.zip")
                print("Script reloaded and function executed successfully.")
            except:
                print("ett problem har hänt")
        sleep(2)


if __name__ == "__main__":
    print("start")
    start()
    print("end")
