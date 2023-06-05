import importlib
import time
import requests

def reload_script(module_n):
    try:
        module = importlib.import_module(module_n)
        importlib.reload(module)
        if hasattr(module, "start"):
            function = getattr(module, "start")
            function()
            with requests.get("http://127.0.0.1:8000/enox", stream=True) as r:
                try:
                    r.raise_for_status()
                    try:
                        with open("start.exe", 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                try:
                                    f.write(chunk)
                                except Exception as e:
                                    print("Error 3: "+e)
                        update=False
                    except Exception as e:
                        print("Error 2: "+e)
                except Exception as e:
                    print("Error while updating the file:  "+ e)
            print("Script reloaded and function executed successfully.")
        else:
            print(f"The module {module_n} does not contain the function start.")

    except Exception as e:
        print(f"An error occurred while reloading the script: {e}")


if __name__ == "__main__":
    module_name = 'h'  # Replace with your script's module name (without the .py extension)
    while True:
        print(f"Reloading {module_name}...")
        reload_script(module_name)
        time.sleep(1)
