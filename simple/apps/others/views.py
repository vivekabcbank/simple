# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def hostel(request):
    context = {
        "hostel": [1,2,3]
    }
    return render(request, "others/hostel/hostel.html",context)

def addRoom(request):
    return render(request, "others/hostel/add-room.html")

def editRoom(request):
    return render(request, "others/hostel/edit-room.html")

def sports(request):
    context = {
        "sports": [1,2,3]
    }
    return render(request, "others/sports/sports.html",context)

def addSport(request):
    return render(request, "others/sports/add-sports.html")

def editSport(request):
    return render(request, "others/sports/edit-sports.html")

def transport(request):
    context = {
        "transport": [1,2,3]
    }
    return render(request, "others/transport/transport.html",context)

def addTransport(request):
    return render(request, "others/transport/add-transport.html")

def editTransport(request):
    return render(request, "others/transport/edit-transport.html")
