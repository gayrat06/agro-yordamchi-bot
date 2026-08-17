import requests

# OpenWeatherMap bepul API kaliti (bepul va ochiq servis orqali)
def get_weather(city: str = "Manghit"):
    try:
        # Mang'it / Amudaryo ko'rsatkichlari uchun open-meteo bepul servisidan foydalanamiz (API key talab qilmaydi)
        url = "https://api.open-meteo.com/v1/forecast?latitude=42.1156&longitude=60.0594&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        current = data.get("current", {})
        temp = current.get("temperature_2m", "N/A")
        humidity = current.get("relative_humidity_2m", "N/A")
        wind = current.get("wind_speed_10m", "N/A")
        
        text = (
            f"🌤 **Mang'it va Amudaryo tumanidagi ob-havo:**\n\n"
            f"🌡 **Harorat:** {temp} °C\n"
            f"💧 **Havo namligi:** {humidity} %\n"
            f"💨 **Shamol tezligi:** {wind} km/soat\n\n"
            f"💡 *Dehqonlarga tavsiya:* Shamol tezligi yuqori bo'lsa, purkash ishlarini (pestitsid/o'g'it) vaqtincha to'xtatib turgan ma'qul."
        )
        return text
    except Exception as e:
        return "⚠️ Ob-havo ma'lumotlarini olishda xatolik yuz berdi."