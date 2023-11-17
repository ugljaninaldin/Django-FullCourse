from django.urls import path
from . import views

app_name = "models4"
urlpatterns = [
    path("", views.models4, name="models4"),
]