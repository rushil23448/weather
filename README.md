# 🌧️ Weather App

A beautiful, simple Python weather application that shows real-time weather updates using the OpenWeather API. Designed with a clean and responsive UI to ensure a seamless user experience.

---

## 📊 Project Structure

```bash
OST_PROJECT/
├── OST_project/
│   ├── __pycache__/
│   ├── background.jpg
│   ├── config.py
│   ├── ui.py
│   ├── utils.py
│   ├── weather_api.py
│   └── main.py
├── requirements.txt
└── run_weather_app.sh
```

---

## ✨ Features

- ✅ Real-time weather data fetching.
- ✅ Displays Temperature, Weather Condition, Humidity, Wind Speed.
- ✅ Sleek, image-based background.
- ✅ Modular code structure for easy maintenance.
- ✅ Virtual environment setup for dependency management.

---

## 🔧 Setup and Installation

### Step 1: Clone the repository
```bash
git clone <repository_link>
cd OST_PROJECT
```

### Step 2: Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up your API key
- Open `config.py`.
- Replace:
  ```python
  API_KEY = "your_openweather_api_key_here"
  ```
  with your **actual API key** from [OpenWeather](https://openweathermap.org/).

### Step 5: Run the Application
```bash
python main.py
```

### (Optional) Run via Shell Script
```bash
./run_weather_app.sh
```

---

## 📊 Expected vs Actual Output

| Criteria                | Expected Outcome                                | Actual Outcome                                     |
|--------------------------|--------------------------------------------------|----------------------------------------------------|
| Weather Data             | Real-time, accurate info                        | Mostly accurate with minor 1-2°C discrepancies    |
| UI Responsiveness        | Smooth, clean background, organized display     | Fully matched                                      |
| Error Handling           | Proper messages for invalid input               | Works as intended                                 |

> Minor accuracy issues were observed due to API refresh rates, but overall, the app performed exceptionally.

---

## 👨‍💻 Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Requests** (API Calls)
- **OpenWeather API**

---

## 📚 License

This project is intended for educational and personal use only.

---

## 💖 Acknowledgements
- [OpenWeather](https://openweathermap.org/) for providing accessible and detailed weather data APIs.

---

> Made with ❤️ for learning and innovation!

