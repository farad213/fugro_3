from django.urls import path
from . import views

urlpatterns = [
    path('buildings', views.buildings, name="sisecam_buildings"),
    path("ajax/buildings/select", views.ajax_buildings_select, name="ajax_buildings_select"),
    path("ajax/buildings/calculate", views.ajax_buildings_calculate, name="ajax_calculate_url")
]