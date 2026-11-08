from pathlib import Path
import json, os

class save:

    def __init__(self,player_class_name="Default",path = os.environ['HOME']):
        self.abs_path = f"{path}/.{player_class_name}.json" #Create the absolute path for the file

    def do_exist(self): #Return boolean if file exist or not
        return Path(self.abs_path).is_file()

    def create(self): #Create teh save file
            with open(self.abs_path, "x"):...

    def write(self, data):
        if not self.do_exist() : #Check first if the file is already there
            raise FileNotFoundError("Player not found, did you called create() for this player ?")
        with open(self.abs_path, "w") as file:
            json.dump(data, file)

    def fetch(self):    #Fetch all the data written in the file.
        with open (self.abs_path, "r") as file:
            return dict(json.load(file))
