from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CreateL0", views.CreateL0, name="CreateL0"), 
    path("CreateL1", views.CreateL1, name="CreateL1"), 
    path("CreateL2", views.CreateL2, name="CreateL2"), 
    path("CreateL3", views.CreateL3, name="CreateL3"), 
    path("CreateL4", views.CreateL4, name="CreateL4"), 
    path("CreateL5", views.CreateL5, name="CreateL5"), 
    
]
