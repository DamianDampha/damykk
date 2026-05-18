"""Views for the weather app - Gambia Weather Tracker."""
from django.shortcuts import render, get_object_or_404
from .models import City, WeatherData, Forecast, WeatherAlert


def home(request):
    """Homepage with current weather overview."""
    cities = City.objects.all()
    weather_data = WeatherData.objects.select_related('city')
    alerts = WeatherAlert.objects.filter(is_active=True)[:5]
    
    context = {
        'cities': cities,
        'weather_data': weather_data,
        'alerts': alerts,
    }
    return render(request, 'blog/home.html', context)


def city_weather(request, pk):
    """Display weather details for a specific city."""
    city = get_object_or_404(City, pk=pk)
    weather = WeatherData.objects.get(city=city) if WeatherData.objects.filter(city=city).exists() else None
    forecast = Forecast.objects.filter(city=city)[:7]
    alerts = WeatherAlert.objects.filter(city=city, is_active=True)
    
    context = {
        'city': city,
        'weather': weather,
        'forecast': forecast,
        'alerts': alerts,
    }
    return render(request, 'blog/city_weather.html', context)


def cities_list(request):
    """List all cities in Gambia with their weather."""
    cities = City.objects.prefetch_related('current_weather').all()
    
    context = {
        'cities': cities,
    }
    return render(request, 'blog/cities_list.html', context)


def forecast_view(request):
    """Display weather forecasts for all cities."""
    cities = City.objects.all()
    forecasts = Forecast.objects.select_related('city').order_by('city', 'date')[:28]
    
    context = {
        'cities': cities,
        'forecasts': forecasts,
    }
    return render(request, 'blog/forecast.html', context)


def alerts_view(request):
    """Display active weather alerts."""
    alerts = WeatherAlert.objects.filter(is_active=True).select_related('city').order_by('-issued_at')
    
    context = {
        'alerts': alerts,
    }
    return render(request, 'blog/alerts.html', context)


def about(request):
    """About page."""
    return render(request, 'blog/about.html')


def contact(request):
    """Contact page."""
    return render(request, 'blog/contact.html')
