import requests
from win10toast import ToastNotifier
import time

toast = ToastNotifier()

def update():
    while True:
        try:
            r = requests.get("https://disease.sh/v3/covid-19/all", timeout=5)
            if r.status_code == 200:
                data = r.json()
                text = f"Confirmed: {data['cases']}\nDeaths: {data['deaths']}\nRecovered: {data['recovered']}"
                toast.show_toast("COVID-19 Update", text, duration=10)
            else:
                toast.show_toast("Error", f"API Error {r.status_code}", duration=10)
        except requests.exceptions.RequestException as e:
            toast.show_toast("Network Error", str(e), duration=10)
        except ValueError:
            toast.show_toast("Parse Error", "Response not in JSON format", duration=10)

        time.sleep(3600)  # every hour

update()


