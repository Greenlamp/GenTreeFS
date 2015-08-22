import os
import sys
import json
import re
import subprocess

path = "C:\\Users\\Greenlamp\\Documents\\Python\\GenTreeFS\\Vault3.sav"
    
def main(text):
    if(isBase64String(text)):
        exe(text)
    file = open(path, "r")
    data = json.load(file)
    dwellers = data["dwellers"]["dwellers"]
    dwellers_count = len(dwellers)
    print(str(dwellers_count) + " dwellers found.")
    for idx, dweller in enumerate(dwellers):
        print("---------------")
        print(dweller["name"] + " " + dweller["lastName"])
        print("---------------")
        print("Babies:")
        print(dweller["relations"]["ascendants"])
        print("---------------")
        print()
    
    
def isBase64String(text):
    text = text.strip()
    length = len(text)
    pattern = "^[a-zA-Z0-9\+/]*={0,3}$"
    result = re.match(pattern, text)
    
    return (length % 4 == 0) and (result)
    
def exe(encryptedText):
    subprocess.call(['C:\\Users\\Greenlamp\\Documents\\Python\\GenTreeFS\\FOSDecrypt.exe', 'C:\\Users\\Greenlamp\\Documents\\Python\\GenTreeFS\\Vault3.sav'])

            

if __name__ == "__main__":
    file = open(path, "r")
    main(file.read())