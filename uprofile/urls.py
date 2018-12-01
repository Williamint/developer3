
from django.urls import path
from uprofile import views

urlpatterns = [
    path('', views.index, name = 'index')
]
