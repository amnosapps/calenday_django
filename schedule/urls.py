from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/schedules", views.schedules, name="schedules"),
]
