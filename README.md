🌦️ Weather App
A simple and elegant weather application that fetches real-time weather data using the OpenWeather API and displays it in a user-friendly interface.

📂 Project Structure


OST_PROJECT/
│
├── OST_project/
│   ├── __pycache__/
│   ├── background.jpg
│   ├── config.py
│   ├── ui.py
│   ├── utils.py
│   ├── weather_api.py
│   └── main.py
│
├── requirements.txt
└── run_weather_app.sh (optional setup script)
⚙️ Features
Fetches real-time weather data from OpenWeather.

Displays:

Temperature

Weather conditions (clear, rainy, cloudy, etc.)

Humidity

Wind speed

Clean and responsive graphical interface.

Simple to use and easy to customize.

🛠️ Setup Instructions
Clone the repository or download the project folder.

Navigate to the project directory:

cd OST_PROJECT
Create a virtual environment:


python3 -m venv venv
Activate the virtual environment:


source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Set your OpenWeather API key:

Open config.py and replace:

python
Copy
Edit
API_KEY = "your_openweather_api_key_here"
with your actual API key from OpenWeather.

Run the app:

bash
Copy
Edit
python main.py
(Optional) Run using the shell script:


./run_weather_app.sh
📈 Expected vs Actual Output
The app successfully fetches and displays the weather details for any valid city entered.

Minor variations (1–2°C) were observed compared to other sources, mainly due to API update frequency and data latency, but overall functionality aligned perfectly with the expectations.

🔥 Technologies Used
Python 3

Tkinter for the user interface

OpenWeather API for weather data

Requests for API calls

📄 License
This project is for educational purposes only.

