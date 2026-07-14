from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel


class AlarmPopup:


    def __init__(self, audio):

        self.audio = audio
    
        self.dialog = None



    def show(self, prayer):


        if self.dialog:

            return



        self.dialog = MDDialog(

            title="🕌 Prayer Time",

            text=f"It is time for {prayer} prayer",

            buttons=[

                MDFlatButton(

                    text="STOP",

                    on_release=lambda x:self.close()

                ),


                MDFlatButton(

                    text="SNOOZE",

                    on_release=lambda x:self.snooze()

                )

            ]

        )


        self.dialog.open()



    def close(self):

        self.audio.stop()
    
        if self.dialog:
    
            self.dialog.dismiss()
    
            self.dialog = None



    def snooze(self):

        print("Alarm snoozed for 5 minutes")

        self.close()