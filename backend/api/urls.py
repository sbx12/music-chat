from django.urls import path
from api import views


urlpatterns = [
    path('room', views.RoomView.as_view()),
]
