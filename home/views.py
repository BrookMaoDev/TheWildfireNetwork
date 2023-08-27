from django.shortcuts import render
from django import forms
from . import util
from . import news


def index(request):
    news_list = news.getFeed("canada")
    return render(
        request,
        "home/index.html",
        {"news_list": news_list},
    )


def predict(request):
    if request.method == "POST":
        # verify if city and postal are valid
        form = predictForm(request.POST)
        if form.is_valid():
            request.session["postal"] = form.cleaned_data["postal"]
            request.session["city"] = form.cleaned_data["city"]

    location = util.Location(request.session["city"], request.session["postal"])
    forecast = location.getForecast()

    temp_c = forecast["current"]["temp_c"]
    humidity = forecast["current"]["humidity"]
    wind_kph = forecast["current"]["wind_kph"]

    fireRisk = location.calculateFireRisk(temp_c, humidity, wind_kph)

    return render(
        request,
        "home/predict.html",
        {
            "predictForm": predictForm(),
            "text": forecast["current"]["condition"]["text"],
            "temp_c": temp_c,
            "humidity": humidity,
            "wind_kph": wind_kph,
            "precip_mm": forecast["current"]["precip_mm"],
            "name": forecast["location"]["name"],
            "country": forecast["location"]["country"],
            "message": fireRisk,
        },
    )


class predictForm(forms.Form):
    postal = forms.CharField(label="Postal Code", required=False)
    city = forms.CharField(label="City", required=False)


def about(request):
    return render(request, "home/about.html")
