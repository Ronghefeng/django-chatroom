from django.shortcuts import render

from django.views.generic import View


def index(request):
    return render(request, "chat/index.html", {})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


class TestView(View):
    pass
