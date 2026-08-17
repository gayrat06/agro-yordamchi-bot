import requests

def get_weather():
    try:
        # Bepul va kalitsiz Open-Meteo API
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 42.1156,
            "longitude": 60.0594,
            "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
            "timezone": "auto"
        }
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        
        if "current" in data:
            current = data["current"]
            temp = current.get("temperature_2m", "N/A")
            humidity = current.get("relative_humidity_2m", "N/A")
            wind = current.get("wind_speed_10m", "N/A")
            
            return (
                f"🌤 **Mang'it va Amudaryo tumanidagi ob-havo:**\n\n"
                f"🌡 **Harorat:** {temp} °C\n"
                f"💧 **Havo namligi:** {humidity} %\n"
                f"💨 **Shamol tezligi:** {wind} km/soat\n\n"
                f"💡 *Dehqonlarga tavsiya:* Shamol tezligi yuqori bo'lsa, purkash ishlarini (pestitsid/o'g'it) vaqtincha to'xtatib turgan ma'qul."
            )
        else:
            return "⚠️ Ob-havo ma'lumotlarini olishda xatolik yuz berdi."
            
    except Exception as e:
        return f"⚠️ Ob-havo serveriga ulanishda xatolik: {str(e)}"