import requests
from django.shortcuts import render
from .models import Location, WeatherRecord
from django.conf import settings

def get_weather_data(location):
    API_KEY = settings.WEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def index(request):
    locations = Location.objects.all()
    
    if request.method == 'POST':
        location_id = request.POST.get('location')
        location = Location.objects.get(id=location_id)
        weather_data = get_weather_data(location)
        
        # Save weather data to database
        weather_record = WeatherRecord(
            location=location,
            temperature=weather_data['main']['temp'],
            humidity=weather_data['main']['humidity'],
            wind_speed=weather_data['wind']['speed'],
            description=weather_data['weather'][0]['description'],
            weather_icon=weather_data['weather'][0]['icon']
        )
        weather_record.save()
        
        return render(request, 'weather/forecast.html', {
            'weather': weather_record,
            'location': location
        })
    
    return render(request, 'weather/index.html', {'locations': locations})

def forecast_history(request, location_id):
    location = Location.objects.get(id=location_id)
    forecasts = WeatherRecord.objects.filter(location=location).order_by('-recorded_at')[:10]
    return render(request, 'weather/history.html', {
        'location': location,
        'forecasts': forecasts
    })