from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CreateL0", views.CreateL0, name="CreateL0"), 
    
]
