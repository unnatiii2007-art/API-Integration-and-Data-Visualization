import requests
import matplotlib.pyplot as plt

# 🔑 Replace with your API key
API_KEY = "bc3a1da064be7a54ef99d98abf795d39"

# 🌍 City name
city = "Kolkata"

# 🌐 API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

# 📡 Fetch data
response = requests.get(url)
data = response.json()

# 🧾 Extract temperature data
dates = []
temps = []

for item in data["list"][:10]:  # first 10 records
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])

# 📊 Plot graph
plt.figure()
plt.plot(dates, temps, marker='o')
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast - {city}")
plt.tight_layout()

# 💾 Save graph
plt.savefig("weather_report.png")

# 📢 Show graph
plt.show()
