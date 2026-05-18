"""URL configuration for the weather app."""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.cities_list, name='cities_list'),
    path('city/<int:pk>/', views.city_weather, name='city_weather'),
    path('forecast/', views.forecast_view, name='forecast'),
    path('alerts/', views.alerts_view, name='alerts'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
