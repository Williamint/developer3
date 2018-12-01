
from django.urls import path
from gchat import views

urlpatterns = [
    path('', views.index, name = 'index'),
]