from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("coaching index")


def posts(request):
    return HttpResponse("coaching posts")


def post(request, post_id=1):
    return HttpResponse(f"coaching post by id={post_id}")
