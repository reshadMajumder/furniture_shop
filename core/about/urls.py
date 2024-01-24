from django.urls import path,include
from .views import about
urlpatterns = [
    path('',about,name='about'),
]