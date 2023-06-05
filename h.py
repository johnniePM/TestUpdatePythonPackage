from importlib import reload
from time import sleep
import requests
import json


# from reloading import reloading


def start():
    update=True
    while update:
        version = 6
        req = requests.post("http://127.0.0.1:8000")
        req_ver = json.loads(req.text)["pk"]
        req_enox = requests.get("http://127.0.0.1:8000/enox")
        if req_ver > version:
            update=False

        print("__________________Start__________________")
        print("req_ver " + str(req_ver))
        print(req_ver >= version)
        print("version " + str(version))
        print("__________________End____________________\n\n\n\n")

        sleep(2)
