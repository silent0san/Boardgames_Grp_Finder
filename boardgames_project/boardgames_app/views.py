from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("elo")
    return render(request, 'boardgames_app/home.html')


def test_view(request):
    return render(request, "boardgames_app/test_view.html")

