from django.urls import path
from .views import Leslita


urlpatterns = [

    path('', Leslita, name = "leslita"),
]