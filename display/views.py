from django.shortcuts import render
from .models import Display

# Create your views here.

def home(request):
    display = Display.objects.all
    return render(request, "home.html", {'display':display})