from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('<slug:month>', views.process_month)
]