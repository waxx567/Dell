import requests


"""
Function to validate city name
"""
def validate_city(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    return response.status_code == 200


"""
Function to retrieve the weather data from the OpenWeatherMap API
"""
def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    return data


"""
Function to display an emoji that best describes the weather conditions
"""
def display_weather_emoji(weather_data):
    description = weather_data['weather'][0]['description']

    if 'cloud' in description:
        print('🌥️')
    elif 'rain' in description:
        print('🌧️')
    elif 'sun' in description or 'clear' in description:
        print('🌞')
    else:
        pass


"""
Function to format the weather data to make it easy to read
"""
def format_weather(weather_data):
    city_name = weather_data['name']
    country_code = weather_data['sys']['country']
    country_name = get_country_name(country_code)
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp'] - 273.15
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']

    formatted_weather = f"Weather in {city_name}, {country_name}:\n"
    formatted_weather += f"Description: {description}\n"
    formatted_weather += f"Temperature: {temperature:.2f}°C\n"
    formatted_weather += f"Humidity: {humidity}%\n"
    formatted_weather += f"Wind speed: {wind} m/s\n"

    return formatted_weather


"""
Function to get the country's code from the country code
"""
def get_country_name(country_code):
    country_info_api = f"https://restcountries.com/v2/alpha/{country_code}"
    response = requests.get(country_info_api)

    if response.status_code == 200:
        country_data = response.json()
        return country_data.get('name', country_code)
    else:
        return country_code


def main():
    api_key = "88e48e2416af614c0705bccdeec9d75b"

    '''Error check the city name'''
    while True:
        city = input("Name of city: ").strip()
        if city.isalpha() and city.istitle():
            if validate_city(api_key, city):
                break
            else:
                ("Invalid city name. Please enter a valid city name.")
        else:
            print("Please enter a valid city name with the first letter capitalized.")

    '''Call the function to get the weather information'''
    weather_data = get_weather(api_key, city)
    print(weather_data)
    '''Call the function to assign the emoji'''
    display_weather_emoji(weather_data)
    '''Call the function to format the weather information'''
    formatted_data = format_weather(weather_data)
    '''Display the requested weather information'''
    print(formatted_data)


if __name__ == "__main__":
    main()
