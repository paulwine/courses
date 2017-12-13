# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *


def index(request):
    all_users = Course.objects.all()
    context = {
        "all_users" : all_users
    }
    print all_users
    return render(request, 'index.html', context)

def add_course(request):
    name = request.POST["name"]
    desc = request.POST["name"]
    Course.objects.create(name=name, desc=desc)
    return redirect("/")
# Create your views here.
