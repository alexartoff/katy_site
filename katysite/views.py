from django.shortcuts import render

# Create your views here.
from katysite.models import MainMenu


def index(request):
    menu = MainMenu.objects.all()
    data = {
        'menu': menu,
    }
    return render(request, "index.html", context=data)
