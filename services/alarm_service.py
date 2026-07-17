from datetime import datetime, timedelta


class AlarmService:

    def get_next_prayer(self, prayers):
        now = datetime.now()

        prayer_list = []

        for name, time in prayers.items():

            hour, minute = map(int, time.split(":")[:2])

            prayer_time = now.replace(
                hour=hour,
                minute=minute,
                second=0,
                microsecond=0
            )

            # If today's prayer has already passed,
            # schedule it for tomorrow.
            if prayer_time <= now:
                prayer_time += timedelta(days=1)

            prayer_list.append((name, prayer_time))

        prayer_list.sort(key=lambda x: x[1])

        return prayer_list[0]

    def countdown(self, target):

        now = datetime.now()

        difference = target - now

        seconds = int(difference.total_seconds())

        if seconds < 0:
            return "00:00:00"

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        sec = seconds % 60

        return f"{hours:02}:{minutes:02}:{sec:02}"

    def check_alarm(self, prayers):

        now = datetime.now().strftime("%H:%M")

        for name, time in prayers.items():

            if now == time:
                return name

        return None