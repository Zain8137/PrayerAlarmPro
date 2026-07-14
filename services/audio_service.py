import os

from kivy.core.audio import SoundLoader
from kivy.resources import resource_find


class AudioService:


    def __init__(self):

        self.current_sound = None


        self.prayer_sounds = {

            "Fajr": resource_find(
                "assets/alarms/azan1.mp3"
            ),

            "Dhuhr": resource_find(
                "assets/alarms/azan2.mp3"
            ),

            "Asr": resource_find(
                "assets/alarms/azan3.mp3"
            ),

            "Maghrib": resource_find(
                "assets/alarms/azan4.mp3"
            ),

            "Isha": resource_find(
                "assets/alarms/azan5.mp3"
            )

        }



        self.test_sounds = {

            "Alarm1": resource_find(
                "assets/sounds/alarm1.mp3"
            ),

            "Alarm2": resource_find(
                "assets/sounds/alarm2.mp3"
            ),

            "Alarm3": resource_find(
                "assets/sounds/alarm3.mp3"
            ),

            "Alarm4": resource_find(
                "assets/sounds/alarm4.mp3"
            ),

            "Alarm5": resource_find(
                "assets/sounds/alarm5.mp3"
            )

        }



    # -------------------------------
    # Play Prayer Azan
    # -------------------------------

    def play_prayer(self, prayer):


        if prayer not in self.prayer_sounds:
            print("No sound found:", prayer)
            return



        file = self.prayer_sounds[prayer]


        if not file:

            print(
                "Audio file missing:",
                prayer
            )

            return



        self.stop()



        self.current_sound = SoundLoader.load(
            file
        )


        if self.current_sound:

            self.current_sound.volume = 1

            self.current_sound.play()


            print(
                "Playing Azan:",
                prayer
            )



    # -------------------------------
    # Play Normal Alarm
    # -------------------------------

    def play_alarm(self, alarm_name="Alarm1"):


        if alarm_name not in self.test_sounds:

            print(
                "Alarm not found:",
                alarm_name
            )

            return



        file = self.test_sounds[alarm_name]



        if not file:

            print(
                "Alarm file missing:",
                alarm_name
            )

            return



        self.stop()



        self.current_sound = SoundLoader.load(
            file
        )


        if self.current_sound:

            self.current_sound.volume = 1

            self.current_sound.play()



            print(
                "Playing alarm:",
                alarm_name
            )



    # -------------------------------
    # Stop Sound
    # -------------------------------

    def stop(self):


        if self.current_sound:


            self.current_sound.stop()


            self.current_sound = None



    # -------------------------------
    # Loop Alarm (for prayer alarm)
    # -------------------------------

    def play_loop(self, prayer):


        if prayer not in self.prayer_sounds:

            return



        file = self.prayer_sounds[prayer]


        self.stop()



        self.current_sound = SoundLoader.load(
            file
        )



        if self.current_sound:


            self.current_sound.loop = True

            self.current_sound.volume = 1

            self.current_sound.play()



            print(
                "Looping:",
                prayer
            )