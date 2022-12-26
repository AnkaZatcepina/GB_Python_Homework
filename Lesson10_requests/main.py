import requests

def get_weather_by_city(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=5ad7b8fca6310aff7d3bdd2d7d6a2631&units=metric&lang=ru"
    r = requests.get(url)
    data = r.json()
    if data["cod"] == 200:
        print(f"В городе {data['name']} сегодня {data['weather'][0]['description']}.")
        print(f"Средняя температура {data['main']['temp']} °C, по ощущениям {data['main']['feels_like']} °C")
        print(f"Скорость ветра {data['wind']['speed']} м/с")
        print(f"Атмосферное давление {data['main']['pressure']} мм рт. ст., влажность {data['main']['humidity']}%")
    else:
        print(f"Ошибка для {city_name}: {data['message']}")  

#city_name = input("Введите название города: ")
get_weather_by_city("Москва")
print()
get_weather_by_city("london")
print()
get_weather_by_city("анапа")
print()
get_weather_by_city("несуществующий город")
