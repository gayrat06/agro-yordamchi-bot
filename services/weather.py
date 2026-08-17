import requests

def get_weather():
    try:
        # Mang'it va Amudaryo koordinatalari uchun so'rov
        url = "https://api.open-meteo.com/v1/forecast?latitude=42.1156&longitude=60.0594&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if "current" in data:
            current = data["current"]
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
        else:
            return "⚠️ Ob-havo ma'lumotlarini olishda xatolik yuz berdi."
            
    except Exception as e:
        return "⚠️ Ob-havo serveriga ulanishda xatolik yuz berdi."