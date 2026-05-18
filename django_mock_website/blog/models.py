"""Database models for the weather app - Gambia Weather Tracker."""
from django.db import models


class City(models.Model):
    """Cities in Gambia."""
    name = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f"{self.name}, {self.region}"


class WeatherData(models.Model):
    """Current weather data for cities in Gambia."""
    CONDITION_CHOICES = [
        ('sunny', '☀️ Sunny'),
        ('cloudy', '☁️ Cloudy'),
        ('rainy', '🌧️ Rainy'),
        ('stormy', '⛈️ Stormy'),
        ('humid', '💨 Humid'),
        ('hazy', '🌫️ Hazy'),
    ]

    city = models.OneToOneField(City, on_delete=models.CASCADE, related_name='current_weather')
    temperature = models.FloatField(help_text="Temperature in Celsius")
    feels_like = models.FloatField(help_text="Feels like temperature in Celsius")
    humidity = models.IntegerField(help_text="Humidity percentage (0-100)")
    wind_speed = models.FloatField(help_text="Wind speed in km/h")
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather in {self.city.name}"


class Forecast(models.Model):
    """Weather forecast for cities."""
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='forecasts')
    date = models.DateField()
    high_temp = models.FloatField()
    low_temp = models.FloatField()
    condition = models.CharField(max_length=20, choices=WeatherData.CONDITION_CHOICES)
    rainfall_chance = models.IntegerField(default=0, help_text="Chance of rain (0-100)")
    wind_speed = models.FloatField()

    class Meta:
        ordering = ['date']
        unique_together = ['city', 'date']

    def __str__(self):
        return f"{self.city.name} - {self.date}"


class WeatherAlert(models.Model):
    """Weather alerts and warnings for Gambia."""
    ALERT_LEVELS = [
        ('info', 'ℹ️ Information'),
        ('warning', '⚠️ Warning'),
        ('alert', '🚨 Alert'),
    ]

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='alerts')
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=ALERT_LEVELS)
    issued_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-issued_at']

    def __str__(self):
        return f"{self.title} - {self.city.name}"
