from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform

import threading

from screens.home import HomeScreen
from services.background_service import BackgroundPrayerService


# Mobile preview only
if platform != "android":
    Window.size = (360, 720)



class PrayerAlarmApp(MDApp):


    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"


        Builder.load_file("kv/home.kv")


        sm = ScreenManager()


        self.home = HomeScreen(
            name="home"
        )


        sm.add_widget(self.home)


        # Load prayer data
        self.home.load_prayer_times()


        return sm



    def on_start(self):

        self.background_service = BackgroundPrayerService()


        self.thread = threading.Thread(
            target=self.background_service.run,
            daemon=True
        )


        self.thread.start()



if __name__ == "__main__":

    PrayerAlarmApp().run()