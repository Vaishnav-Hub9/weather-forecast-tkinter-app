import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    place = place_entry.get()
    if not place:
        messagebox.showerror("Error", "Please enter a place name!")
        return
    
    api_key = "ENTER_YOUR_API_KEY_FROM_OPEN_WEATHER_MAP"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": place, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        result_label.config(
            text=f"📍 Place: {place}\n"
                 f"🌡 Temperature: {temperature}°C\n"
                 f"☁ Weather: {description}\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌬 Wind Speed: {wind_speed} m/s"
        )

    except Exception:
        messagebox.showerror("Error", "Failed to fetch weather data")


# Window setup
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("700x500")
window.configure(bg="#f0f0f0")

# CENTER FRAME
main_frame = tk.Frame(window, bg="#f0f0f0")
main_frame.pack(expand=True)

# Widgets
tk.Label(main_frame, text="Enter a Place", font=("Helvetica", 16, "bold"),
         fg="#333", bg="#f0f0f0").pack(pady=10)

place_entry = tk.Entry(main_frame, font=("Helvetica", 14), width=25, justify="center")
place_entry.pack(pady=10)

tk.Button(main_frame, text="Get Weather Data", command=get_weather,
          font=("Helvetica", 14), bg="#ffa500", fg="black",
          relief="raised", padx=10, pady=5).pack(pady=15)

result_label = tk.Label(main_frame, text="", font=("Helvetica", 14),
                        justify="left", bg="#ffffff", fg="#000",
                        width=40, height=8, bd=2, relief="groove")
result_label.pack(pady=20)

window.mainloop()

