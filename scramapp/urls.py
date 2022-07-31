from django.contrib import admin
from django.urls import path
from scramapp.views import home_view
urlpatterns = [
    path('', home_view, name = 'home_view'),
]