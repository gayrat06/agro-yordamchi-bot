import requests

def get_weather():
    try:
        # Mang'it / Amudaryo koordinatalari (42.1156, 60.0594)
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 42.1156,
            "longitude": 60.0594,
            "current_weather": "true",
            "timezone": "auto"
        }
        
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if "current_weather" in data:
            current = data["current_weather"]
            temp = current.get("temperature", "N/A")
            wind = current.get("windspeed", "N/A")
            
            text = (
                f"🌤 **Mang'it va Amudaryo tumanidagi ob-havo:**\n\n"
                f"🌡 **Harorat:** {temp} °C\n"
                f"💨 **Shamol tezligi:** {wind} km/soat\n\n"
                f"💡 *Dehqonlarga tavsiya:* Shamol tezligi yuqori bo'lsa, purkash ishlarini (pestitsid/o'g'it) vaqtincha to'xtatib turgan ma'qul."
            )
            return text
        else:
            return "⚠️ Ob-havo ma'lumotlarini olishda xatolik yuz berdi."
            
    except Exception as e:
        return "⚠️ Ob-havo serveriga ulanishda xatolik yuz berdi."