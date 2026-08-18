import json
import urllib.request

def get_weather():
    try:
        # Open-Meteo standart URL (Mang'it / Amudaryo)
        url = "https://api.open-meteo.com/v1/forecast?latitude=42.1156&longitude=60.0594&current_weather=true"
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        if "current_weather" in data:
            current = data["current_weather"]
            temp = current.get("temperature", "N/A")
            wind = current.get("windspeed", "N/A")
            
            return (
                f"🌤 **Mang'it va Amudaryo tumanidagi ob-havo:**\n\n"
                f"🌡 **Harorat:** {temp} °C\n"
                f"💨 **Shamol tezligi:** {wind} km/soat\n\n"
                f"💡 *Dehqonlarga tavsiya:* Shamol tezligi yuqori bo'lsa, purkash ishlarini (pestitsid/o'g'it) vaqtincha to'xtatib turgan ma'qul."
            )
        else:
            return "⚠️ Ob-havo ma'lumotlari shakllantirilmadi."
            
    except Exception as e:
        return f"⚠️ Ob-havo serveriga ulanishda xatolik: {e}"