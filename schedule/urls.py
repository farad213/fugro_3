from django.urls import path
from . import views

urlpatterns = [
    path('admin/<int:year>/<int:month>', views.admin, name="admin"),
]