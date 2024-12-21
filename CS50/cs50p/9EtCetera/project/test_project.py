import pytest
from unittest.mock import patch, Mock
from project import validate_city, get_weather, display_weather_emoji, format_weather, get_country_name


@pytest.fixture
def mock_response():
    return Mock()


@pytest.fixture
def mock_get(monkeypatch, mock_response):
    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr('requests.get', mock_get)


def test_validate_city_valid(mock_get, mock_response):
    mock_response.status_code = 200

    api_key = "fake_api_key"
    city = "ValidCity"

    result = validate_city(api_key, city)
    assert result is True


def test_validate_city_invalid(mock_get, mock_response):
    mock_response.status_code = 404

    api_key = "fake_api_key"
    city = "InvalidCity"

    result = validate_city(api_key, city)
    assert result is False


def test_get_weather(mock_get, mock_response):
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'name': 'TestCity',
        'sys': {'country': 'US'},
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 20, 'humidity': 60},
        'wind': {'speed': 3.5}
    }

    api_key = "fake_api_key"
    city = "TestCity"

    result = get_weather(api_key, city)
    assert result['name'] =='TestCity'
    assert result['sys']['country'] == 'US'
    assert result['weather'][0]['description'] == 'clear sky'
    assert result['main']['temp'] == 20
    assert result['main']['humidity'] == 60
    assert result['wind']['speed'] == 3.5


def test_display_weather_emoji(capfd):
    weather_data = {'weather': [{'description': 'clear sky'}]}
    display_weather_emoji(weather_data)
    captured = capfd.readouterr()
    assert '🌞' in captured.out


def test_format_weather():
    weather_data = {
        'name': 'TestCity',
        'sys': {'country': 'US'},
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 20, 'humidity': 60},
        'wind': {'speed': 3.5}
    }

    result = format_weather(weather_data)
    expected_result = "Weather in TestCity, United States of America:\nDescription: clear sky\nTemperature: -253.15°C\nHumidity: 60%\nWind speed: 3.5 m/s\n"
    assert result == expected_result


def test_get_country_name(mock_get, mock_response):
    mock_response.status_code = 200
    mock_response.json.return_value = {'name': 'United States'}

    country_code = 'US'
    result = get_country_name(country_code)
    assert result == 'United States'