import requests
import pathlib
import json
import requests
import csv
import pandas as pd
import time
 

 
 

with open("PandaAEGIS_IOCs.json") as file:
    json_str = file.read()

with open('PandaAEGIS_IOCs.txt', 'a') as f:
    list_obj = json.loads(json_str)
    for i in list_obj["objects"]:
        try:
            f.write(i["pattern"].strip("[ ]" "=" "'" "= '"))
            f.write("\n")
        except KeyError:
            print("key error")
