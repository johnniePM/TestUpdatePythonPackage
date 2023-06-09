from importlib import reload
from time import sleep
import requests
import json
import zipfile

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
        if req_ver > version:
            with requests.get("http://127.0.0.1:8000/enox", stream=True) as r:
                try:
                    r.raise_for_status()
                    try:
                        with open("main.zip", "wb") as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                try:
                                    f.write(chunk)
                                except Exception as e:
                                    print("Error 3: " + e)
                            json.dump({"version": req_ver}, open("version.json", "w"))
                    except Exception as e:
                        print("Error 2: " + e)
                    with zipfile.ZipFile("main.zip") as zip:
                        zip.extractall()
                except Exception as e:
                    print("Error while updating the file:  " + e)
            print("Script reloaded and function executed successfully.")

        sleep(2)


if __name__ == "__main__":
    print("start")
    start()
    print("end")
