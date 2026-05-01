from django.urls import path
from . import views

app_name = "imc"

urlpatterns = [
    path("", views.index, name="index"),
    path("calcular_novo/", views.calcular, name="calcular" ),
]