from django.contrib import admin
from .models import Location, WeatherRecord

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_code', 'latitude', 'longitude')
    search_fields = ('name', 'country_code')

@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'humidity', 'recorded_at')
    list_filter = ('location', 'recorded_at')
    date_hierarchy = 'recorded_at'