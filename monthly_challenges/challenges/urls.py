from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="monthly-challange"),
]
