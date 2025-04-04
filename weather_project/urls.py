from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='weather_index'),
    path('history/<int:location_id>/', views.forecast_history, name='forecast_history'),
]