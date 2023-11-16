from django.urls import path
from . import views

app_name = "models2"
urlpatterns = [
    path('', views.models2, name="models2"),
]
