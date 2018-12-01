
from django.urls import path
from friends import views

urlpatterns = [
    path('', views.index, name = 'index')
]
