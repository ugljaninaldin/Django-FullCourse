from django.urls import path, include
from . import views

app_name = "models5"
urlpatterns = [
    path("", views.models5, name="models5")
]