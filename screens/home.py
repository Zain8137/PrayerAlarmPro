from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
from datetime import datetime

from services.prayer_service import PrayerService
from services.alarm_service import AlarmService
from services.audio_service import AudioService

from screens.alarm_popup import AlarmPopup
from utils.database import Database
from kivy.animation import Animation

from services.audio_service import AudioService
from services.notification_service import NotificationService

class HomeScreen(Screen):
    selected_sound = StringProperty("azan1.mp3")

    # -------------------------
    # Display Properties
    # -------------------------

    city = StringProperty(
        "Lahore, Pakistan"
    )


    next_prayer = StringProperty(
        "Loading..."
    )


    countdown = StringProperty(
        "--:--:--"
    )


    fajr = StringProperty("--:--")
    dhuhr = StringProperty("--:--")
    asr = StringProperty("--:--")
    maghrib = StringProperty("--:--")
    isha = StringProperty("--:--")



    # -------------------------
    # Alarm Switches
    # -------------------------

    fajr_alarm = BooleanProperty(True)
    dhuhr_alarm = BooleanProperty(True)
    asr_alarm = BooleanProperty(True)
    maghrib_alarm = BooleanProperty(True)
    isha_alarm = BooleanProperty(True)



    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        # Services

        self.prayer_service = PrayerService()

        self.alarm_service = AlarmService()

        self.audio = AudioService()

        self.notification = NotificationService()

        self.popup = AlarmPopup(self.audio)

        self.database = Database()



        self.prayers = None

        self.target_time = None

        self.alarm_started = False



        # Load saved switches

        settings = self.database.load()


        if settings:

            self.fajr_alarm = settings.get(
                "Fajr",
                True
            )

            self.dhuhr_alarm = settings.get(
                "Dhuhr",
                True
            )

            self.asr_alarm = settings.get(
                "Asr",
                True
            )

            self.maghrib_alarm = settings.get(
                "Maghrib",
                True
            )

            self.isha_alarm = settings.get(
                "Isha",
                True
            )



    # -------------------------
    # Screen Open
    # -------------------------



    # -------------------------
    # Prayer API
    # -------------------------

    def load_prayer_times(self):

        self.prayers = self.prayer_service.get_prayer_times(
            "Lahore",
            "Pakistan"
        )


        print("Prayer Data:", self.prayers)


        if self.prayers:

            self.fajr = self.prayers["Fajr"]
            self.dhuhr = self.prayers["Dhuhr"]
            self.asr = self.prayers["Asr"]
            self.maghrib = self.prayers["Maghrib"]
            self.isha = self.prayers["Isha"]


            self.set_next_prayer()
            Clock.schedule_interval(
                self.update_countdown,
                1
            )


            Clock.schedule_once(
                lambda dt: self.animate_countdown(),
                1
            )




    # -------------------------
    # Next Prayer
    # -------------------------

    def set_next_prayer(self):

        name, time = self.alarm_service.get_next_prayer(
            self.prayers
        )
    
        self.next_prayer = name
    
        self.target_time = time
    
        print(
            "Next Prayer:",
            name,
            time
        )





    # -------------------------
    # Countdown
    # -------------------------

    def update_countdown(self, dt):

        if self.target_time:
    
            remaining = self.alarm_service.countdown(
                self.target_time
            )
    
            self.countdown = remaining





    # -------------------------
    # Alarm Checking
    # -------------------------

    def check_alarms(self, dt):


        if not self.prayers:

            return



        result = self.alarm_service.check_alarm(
            self.prayers
        )



        if result:


            print(
                "Prayer Alarm:",
                result
            )
        
        
            # Play sound
            self.audio.play()

            self.notification.send(result)

            self.popup.show(result)    
                   



    # -------------------------
    # Save Switch Settings
    # -------------------------

    def save_alarm_settings(self):


        data = {


            "Fajr":
            self.fajr_alarm,


            "Dhuhr":
            self.dhuhr_alarm,


            "Asr":
            self.asr_alarm,


            "Maghrib":
            self.maghrib_alarm,


            "Isha":
            self.isha_alarm

        }



        self.database.save(
            data
        )



        print(
            "Alarm settings saved"
        )




    def animate_countdown(self):

        try:
    
            animation = Animation(
                font_size=42,
                duration=0.5
            )
    
            animation += Animation(
                font_size=36,
                duration=0.5
            )
    
            animation.repeat = True
    
            animation.start(
                self.ids.countdown_label
            )
    
        except Exception as e:
    
            print("Animation error:", e)



    def change_sound(self, sound):

        self.audio.select_sound(
            sound
        )



    def change_sound(self, sound):

        self.selected_sound = sound
    
        print("Selected sound:", sound)