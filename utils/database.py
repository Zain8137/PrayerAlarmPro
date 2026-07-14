import json
import os



class Database:


    FILE = "alarm_settings.json"



    def save(self,data):


        with open(
            self.FILE,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )





    def load(self):


        if not os.path.exists(
            self.FILE
        ):

            return {


                "Fajr":True,

                "Dhuhr":True,

                "Asr":True,

                "Maghrib":True,

                "Isha":True

            }



        with open(
            self.FILE,
            "r"
        ) as f:

            return json.load(f)