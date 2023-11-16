from django.urls import path

from . import views

app_name = "models1"
urlpatterns = [
    path('', views.models1, name="models1"),
]
