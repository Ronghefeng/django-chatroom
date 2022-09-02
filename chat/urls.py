from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("test/", views.TestView.as_view()),
    path("<str:room_name>/", views.room, name="room"),
]
