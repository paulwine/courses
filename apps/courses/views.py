# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *


def index(request):
    all_courses = Course.objects.all()
    context = {
        "all_courses" : all_courses
    }
    print all_courses
    return render(request, 'index.html', context)

def add_course(request):
    if request.method == "POST":
        name = request.POST["name"]
        desc = request.POST["desc"]
        Course.objects.create(name=name, desc=desc)
        return redirect("/")
    else:
        return redirect("/")

def delete(request, course_id):
    course = Course.objects.filter(id = course_id)
    course_name = course[0].name
    context = {
        "course_id" : course_id,
        "course_name" : course_name
    }
    request.session["course_id"] = course_id
    return render(request, "delete_confirm.html", context)

def del_process(request):
    Course.objects.filter(id = request.session["course_id"]).delete()
    return redirect("/")
def go_back(request):
    return redirect("/")

# Create your views here.
