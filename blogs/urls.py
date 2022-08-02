from django.urls import path

from . import views

urlpatterns = [
    # this code serves the http response from the views.py
    path("", views.index, name="index"),
]
