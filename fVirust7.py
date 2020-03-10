import requests
import pathlib
import json
import requests
import csv
import pandas as pd
import time
#7:  d5ea49f72d235ca3ad1228c78090b5a9ad84de1d7c5d4921bf90bc4b209e2837 
#2:  412b711e1a01df2a7e633f514f02cbe115ec00cce08509444a0894f1cde9460f
#3   b8260eb82cb13a82e452444cff127586a88fd8f9b0fb647a48d869764f2c5e09

url = 'https://www.virustotal.com/vtapi/v2/url/report'
api=['d5ea49f72d235ca3ad1228c78090b5a9ad84de1d7c5d4921bf90bc4b209e2837','412b711e1a01df2a7e633f514f02cbe115ec00cce08509444a0894f1cde9460f',
'b8260eb82cb13a82e452444cff127586a88fd8f9b0fb647a48d869764f2c5e09', '2df562be9db4655862d70e020657d787acb4a210bafb83d346af52d88a7614c2',
'4d292f442d8fa55e4b533a1a8916e04f2e47b14fc9b140a48b0d17cb834a3a12','d2091379ecc4f5d42c50039c0804bdda9ea742203f7105dba38abf2940835b1d',
'd010286bc4ad6e8edcb49be6d7b9cca6bab8f1a69368d640884cf921703e9632','21e024987eff79ce25e8f08c941ff41289e6e63fd1b0f27c4b470f6baafd36f7',
'eb0069c561c3c69b649582f91d0a94551e4f5612c534c5009fd95b7a69ac6893'] 


#7,2,3,8,9,1,6,4,5
 
c=input("Enter file name:")
def csv_reader(file_obj):
    i=-1
    reader = csv.reader(file_obj)
    for row in reader:
            if i <8:
                params = {'apikey': api[i], 'resource': row}
                try:
                        response = requests.get(url, params=params)
                        a=response.json()['resource']
                        b=response.json()['positives']
                        if b > 1 :
                            with open('rezults.csv', 'a') as f:
                                json.dump(a, f, ensure_ascii=False)
                                f.write('  ')
                                json.dump(b, f, ensure_ascii=False)
                                f.write('\n')
                        else:
                            with open('fails and clears.csv', 'a') as f:
                                f.write(str(row).strip("[ ]'"))
                                f.write('\n')
                        time.sleep(2)
                except Exception:
                    with open('fails and clears.csv', 'a') as f:
                        f.write(str(row).strip("[ ]'"))
                        f.write('\n')
                    time.sleep(2)
                i+=1
                print(str(row))
                print(response)
                
            else:
                i=-1
                params = {'apikey': api[i], 'resource': row}
                try:
                        response = requests.get(url, params=params)
                        a=response.json()['resource']
                        b=response.json()['positives']
                        if b > 1 :
                            with open('rezults.csv', 'a') as f:
                                json.dump(a, f, ensure_ascii=False)
                                f.write('  ')
                                json.dump(b, f, ensure_ascii=False)
                                f.write('\n')
                        else:
                            with open('fails and clears.csv', 'a') as f:
                                f.write(str(row).strip("[ ]'"))
                                f.write('\n')
                        time.sleep(2)
                except Exception:
                    with open('fails and clears.csv', 'a') as f:
                        f.write(str(row).strip("[ ]'"))
                        f.write('\n')
                    time.sleep(2)
                i+=1
                print(str(row))
                print(response)
                
if __name__ == "__main__":
    csv_path = c
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)



 
