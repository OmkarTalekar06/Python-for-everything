import requests

def get_weather(city_name):
    API_KEY = "API_KEY" 
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("Error:", data["error"]["message"])
            return

        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]

        print("City:", city_name)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

if __name__ == "__main__":
    CITY = input("Please Enter city name: ")
    get_weather(CITY)
