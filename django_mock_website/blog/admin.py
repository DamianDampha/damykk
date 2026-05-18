"""Admin configuration for the weather app."""
from django.contrib import admin
from .models import City, WeatherData, Forecast, WeatherAlert


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'latitude', 'longitude']
    search_fields = ['name', 'region']
    ordering = ['name']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature', 'condition', 'humidity', 'wind_speed', 'updated_at']
    list_filter = ['condition', 'updated_at']
    search_fields = ['city__name', 'description']
    readonly_fields = ['updated_at']


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ['city', 'date', 'high_temp', 'low_temp', 'condition', 'rainfall_chance']
    list_filter = ['condition', 'date', 'city']
    search_fields = ['city__name']
    date_hierarchy = 'date'


@admin.register(WeatherAlert)
class WeatherAlertAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'level', 'is_active', 'issued_at']
    list_filter = ['level', 'is_active', 'issued_at']
    search_fields = ['title', 'city__name']
    ordering = ['-issued_at']
