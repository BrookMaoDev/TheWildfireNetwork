from django.shortcuts import render
from . import util


# Create your views here.
def index(request):
    return render(request, "home/index.html", {
        'response': util.response
    })
