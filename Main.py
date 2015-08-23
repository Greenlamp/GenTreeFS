import json
import re
import subprocess
import tkinter as tk
from tkinter import filedialog
from Entities.Dwellers import Dwellers
from decrypt import decrypt_save_file, encrypt_save_file


def main():
    nameFileSave, nameFileJson, folderSave, folderJson, root = getFolder(openFile(path))

    if(isBase64String(openFile(path).read())):
        decrypt_save_file(folderSave + nameFileSave, folderJson + nameFileJson, False)
        
    data = loadData(folderJson + nameFileJson)
    dwellers = initDwellers(data)
    encrypt_save_file(folderJson + nameFileJson, folderSave + nameFileSave)

def getFolder(file):
    nameFileSave = file.name.split("/")[-1]
    nameFileJson = (file.name.split("/")[-1]).split(".sav")[0]+(".json")
    folderSave = file.name.split(nameFileSave)[0]
    folderJson = file.name.split("saves")[0] + "json/"
    root = file.name.split("saves")[0]

    return nameFileSave, nameFileJson, folderSave, folderJson, root

def loadData(pathJson):
    data = json.load(openFile(pathJson))
    return data

def openFile(path):
    return open(path, "r+")

    
    
def initDwellers(data):
    dwellers = Dwellers()
    dataDwellers = data["dwellers"]["dwellers"]
    dwellers.initData(dataDwellers)
    dwellers.showAll()
    dwellers.showAllFamilies()
    return dwellers
    
def isBase64String(text):
    text = text.strip()
    length = len(text)
    pattern = "^[a-zA-Z0-9\+/]*={0,3}$"
    result = re.match(pattern, text)
    
    return (length % 4 == 0) and (result)
    
def exe(encryptedText):
    subprocess.call(['FOSDecrypt.exe', path])

            

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    main()