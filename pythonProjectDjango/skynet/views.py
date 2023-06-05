from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.

def index(request):
    data = {
        "access": 1,
        "service": "home-skynet"
    }
    # data["service"] = request.GET['service']
    if request.GET['service'] == "human":
        raise Http404()
    else:
        return render(request, 'skynet/index.html', context=data)

def other(request):
    return HttpResponse("<h2>hello</h2>")

def other(request, id):
    return HttpResponse(f"<h2>hello</h2>{id}")

def homeSkynet(request):
    return HttpResponse("<p>Вы попали на домашнюю страницу Skynet</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('page not found in skynet')