import tkinter as tk
from weather_api import get_weather
from tkinter import messagebox
from PIL import Image, ImageTk  # You will need to install the pillow library

def create_ui():
    def fetch_weather():
        city = entry.get()
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name")
            return
        weather = get_weather(city)

        if weather['cod'] == 200:
            temp = weather['main']['temp']
            description = weather['weather'][0]['description']
            humidity = weather['main']['humidity']
            wind_speed = weather['wind']['speed']
            icon_code = weather['weather'][0]['icon']

            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

            # Updating the UI with weather data
            result.set(f"Weather in {city}: {temp}°C, {description.capitalize()}")
            details.set(f"Humidity: {humidity}%\nWind Speed: {wind_speed} m/s")

            # Load the weather icon
            icon_img = Image.open(requests.get(icon_url, stream=True).raw)
            icon_img = icon_img.resize((50, 50))  # Resize the icon
            icon_photo = ImageTk.PhotoImage(icon_img)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
        else:
            messagebox.showerror("Error", "City not found. Please try again.")

    root = tk.Tk()
    root.title("Weather App")

    # Set the window size
    root.geometry("400x400")

    # Adding a background image
    background_image = Image.open("background.jpg")  # Add a background image (replace 'background.jpg')
    background_image = background_image.resize((400, 400))  # Resize it to fit the window
    background_photo = ImageTk.PhotoImage(background_image)
    
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # Set the label to cover the entire window

    # Title
    title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), fg="white", bg="black")
    title_label.pack(pady=10)

    # Entry widget for city name
    entry = tk.Entry(root, font=("Arial", 14), width=20)
    entry.pack(pady=10)

    # Button to fetch weather data
    fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=fetch_weather, bg="skyblue", relief="solid")
    fetch_button.pack(pady=5)

    # Label for displaying weather result
    result = tk.StringVar()
    result_label = tk.Label(root, textvariable=result, font=("Arial", 14), fg="white", bg="black")
    result_label.pack(pady=5)

    # Label for displaying detailed weather information
    details = tk.StringVar()
    details_label = tk.Label(root, textvariable=details, font=("Arial", 12), fg="white", bg="black")
    details_label.pack(pady=5)

    # Label for displaying weather icon
    icon_label = tk.Label(root)
    icon_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
