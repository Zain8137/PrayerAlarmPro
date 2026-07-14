import requests


class PrayerService:

    def get_prayer_times(self, city, country):

        url = (
            "https://api.aladhan.com/v1/timingsByCity"
            f"?city={city}&country={country}&method=2"
        )

        try:

            response = requests.get(url)

            data = response.json()

            timings = data["data"]["timings"]

            return {

                "Fajr": timings["Fajr"],
                "Dhuhr": timings["Dhuhr"],
                "Asr": timings["Asr"],
                "Maghrib": timings["Maghrib"],
                "Isha": timings["Isha"]

            }


        except Exception as e:

            print("Prayer API Error:", e)

            return None