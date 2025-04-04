from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    country_code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}, {self.country_code}"

class WeatherRecord(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=200)
    recorded_at = models.DateTimeField(auto_now_add=True)
    weather_icon = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['-recorded_at']
    
    def __str__(self):
        return f"{self.location}: {self.temperature}°C at {self.recorded_at}"