import tkinter as tk
import requests

API_KEY = "31156d7d38905ece9422b57ed6a77d03"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()

    if not city:
        result_label.config(text="Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            result_label.config(text="City not found or API error")
            return

        data = response.json()

        name = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()

        weather_info = f"{name}\n{temp:.1f}°C\n{desc}"
        result_label.config(text=weather_info)

    except requests.exceptions.RequestException:
        result_label.config(text="Error: cannot connect to server")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10, padx=10, fill="x")

btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
btn.pack(pady=5)

result_label = tk.Label(root, font=("Arial", 14), justify="center")
result_label.pack(pady=20, padx=10)

root.mainloop()
