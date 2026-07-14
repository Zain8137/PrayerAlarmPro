from plyer import notification


class NotificationService:


    def send(self, prayer):

        try:

            notification.notify(

                title="🕌 Prayer Alarm",

                message=f"It's time for {prayer} prayer",

                app_name="Prayer Alarm Pro",

                timeout=10

            )

            print("Notification sent:", prayer)


        except Exception as e:

            print("Notification error:", e)