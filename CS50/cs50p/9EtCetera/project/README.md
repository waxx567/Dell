# Weather App Project by Wayne McRae - Johannesburg, South Africa 2023/11/17

## Description

The Weather App project is a Python-based application that provides users with real-time weather information for a specified city. This README.md file aims to provide a comprehensive overview of the project, its functionalities, and the structure of the codebase.

### Project Overview

The Weather App project is designed to allow users to input a city name, retrieve current weather data using the OpenWeatherMap API, and display relevant information such as temperature, humidity, wind speed, and a corresponding weather emoji. The application also includes error checking for valid city names and capitalization.

### Files in the Project

- **project.py:** This file contains the main implementation of the Weather App. It includes functions for validating city names, retrieving weather data, displaying weather emojis, formatting weather information, and converting country codes to country names. The `main()` function is the entry point for running the application.

- **test_project.py:** This file includes unit tests for the functions defined in `project.py`. It utilizes the `unittest` framework for testing various aspects of the application, such as city validation, weather data retrieval, and formatting.

### Functionality

1. **City Validation (`validate_city`):** The `validate_city` function checks the validity of a city name by making an API call to OpenWeatherMap. It returns `True` if the city is valid and `False` otherwise.

2. **Weather Data Retrieval (`get_weather`):** The `get_weather` function fetches weather data for a specified city using the OpenWeatherMap API. It returns a JSON object containing relevant weather information.

3. **Display Weather Emoji (`display_weather_emoji`):** This function prints an emoji corresponding to the weather description. It enhances the user interface by providing a visual representation of the weather conditions.

4. **Format Weather Information (`format_weather`):** The `format_weather` function takes the weather data JSON and creates a formatted string containing essential information like city name, country, description, temperature, humidity, and wind speed.

5. **Get Country Name (`get_country_name`):** This function retrieves the full name of a country based on its country code using the REST Countries API.

### Running the Application

To run the Weather App, the user types `python project.py` from the parent folder in the Command Prompt terminal. This executes the `main()` function in the `project.py` file. Follow the prompt to input a valid city name and view the weather information.

For example, should the user input `Berlin` when prompted, the program will return something like this:

🌥️
Weather in Berlin, Germany:
Description: overcast clouds
Temperature: 4.67°C
Humidity: 83%
Wind speed: 7.15 m/s

### Testing

The `test_project.py` file includes both `unittest` and `pytest` tests to ensure the correctness of the implemented functions.

To run the tests, the user inputs `pytest test_project.py`.

The program will return six green dots `......` and `[100%]` and inform the user that 6 tests were passed.

#### Project Video Demo

To see the Weather App in action, check out the video demo [https://youtu.be/YKBEJVHYLi4].
