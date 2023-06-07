import importlib
import time
import requests
import subprocess
import json

def reload_script(module_n):
    try:
        subprocess.run(["h.exe"])
        req = requests.post("http://127.0.0.1:8000")
        req_ver = json.loads(req.text)["pk"]
        json_file=json.load(open("version.json", "r"))
        version=json_file["version"]
        if req_ver > version:
            with requests.get("http://127.0.0.1:8000/enox", stream=True) as r:
                try:
                    r.raise_for_status()
                    try:
                        with open("h2.exe", 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                try:
                                    f.write(chunk)
                                except Exception as e:
                                    print("Error 3: "+e)
                            json.dump({"version":req_ver}, open("version.json", "w"))
                    except Exception as e:
                        print("Error 2: "+e)
                except Exception as e:
                    print("Error while updating the file:  "+ e)
            print("Script reloaded and function executed successfully.")


    except Exception as e:
        print(f"An error occurred while reloading the script: {e}")


if __name__ == "__main__":
    module_name = 'h'  # Replace with your script's module name (without the .py extension)
    while True:
        print(f"Reloading {module_name}...")
        reload_script(module_name)
        time.sleep(1)
