from django.urls import path
from . import views

app_name = "models3"
urlpatterns = [
    path("", views.models3, name="models3")
]