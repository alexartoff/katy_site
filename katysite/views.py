from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("main index <a href='/coach'>coach</a> <a href='/numero'>numero</a>")
