import os
import sys
import json
import re
import subprocess
import Dweller

path = "C:\\Users\\Greenlamp\\Documents\\GitHub\\GenTreeFS\\Vault3.sav"
    
def main(text):
    if(isBase64String(text)):
        exe(text)
        
    data = loadData(text)
    dwellers = initDwellers(data)
    
def loadData(text):
    file = open(path, "r")
    data = json.load(file)
    return data
    
    
def initDwellers(data):
    dwellers = Dweller.Dwellers()
    dataDwellers = data["dwellers"]["dwellers"]
    
    for idx, dweller in enumerate(dataDwellers):
        newDweller = Dweller.Dweller()
        newDweller.id = dweller["serializeId"]
        newDweller.name = dweller["name"]
        dwellers.add(newDweller)
    

    dwellers.showAll()
    
    return dwellers
    
def isBase64String(text):
    text = text.strip()
    length = len(text)
    pattern = "^[a-zA-Z0-9\+/]*={0,3}$"
    result = re.match(pattern, text)
    
    return (length % 4 == 0) and (result)
    
def exe(encryptedText):
    subprocess.call(['C:\\Users\\Greenlamp\\Documents\\GitHub\\GenTreeFS\\FOSDecrypt.exe', 'C:\\Users\\Greenlamp\\Documents\\GitHub\\GenTreeFS\\Vault3.sav'])

            

if __name__ == "__main__":
    file = open(path, "r")
    main(file.read())