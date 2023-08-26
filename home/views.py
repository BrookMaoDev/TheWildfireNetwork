from django.shortcuts import render
from . import util


# Create your views here.
def index(request):
    location = util.Location("Toronto")  # pass city or postal code as param
    return render(request, "home/index.html", {
        'response': location.getForecast()
    })
