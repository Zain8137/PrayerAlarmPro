from datetime import datetime
from time import sleep

from services.prayer_service import PrayerService
from services.alarm_service import AlarmService
from services.audio_service import AudioService


class BackgroundPrayerService:


    def __init__(self):

        self.prayer_service = PrayerService()

        self.alarm_service = AlarmService()

        self.audio = AudioService()



    def run(self):

        print("Background Prayer Service Started")


        prayers = self.prayer_service.get_prayer_times(
            "Lahore",
            "Pakistan"
        )


        while True:


            now = datetime.now().strftime("%H:%M")


            for prayer, time in prayers.items():


                if now == time:


                    print(
                        "Background Alarm:",
                        prayer
                    )


                    self.audio.play()



            sleep(30)