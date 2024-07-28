import os
import random

class CardManager:
    def __init__(self):
        self.appdata_path = os.path.join(os.environ['APPDATA'], "Nihonium")
        os.makedirs(self.appdata_path, exist_ok=True)
        
    def createFile(self, name:str = None) -> str:
        if name == None:
            name = "cardsGroup"+str(random.randint(0, 10000))+".json"
        file_path = os.path.join(self.appdata_path, name)
        with open(file_path, "w") as f:
            f.write(name)
        print(f"File created:" +str(file_path))
        return file_path
    
    def importFile(self, name:str = "cards.json"):
        file_path = os.path.join(self.appdata_path, name)
        with open(file_path, "r") as f:
            for line in f:
                print(line.strip())