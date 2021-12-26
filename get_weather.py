import requests

token = '14fe0948206392dec780b19af1309abd'
def get_weather(data):
    day_num = 0
    if data['city'] == 'msk':
        id = '524894'
        city = 'Москве'
    else:
        id = '498817'
        city = 'Санкт-Петербурге'

    if data['day'] == 'сейчас':
        day_name = 'Сейчас'
    elif data['day'] == 'сегодня':
        day_name = 'Сегодня'
    else:
        day_num = 1
        day_name = 'Завтра'

    if day_num == 1:
        return f'{day_name} в {city} температура будет в районе -5 °C'

    weather_data = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?id={id}&appid={token}&units=metric').json()
    return f'{day_name} в {city} температура будет в районе {weather_data["main"]["temp"]} °C'

