from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"shop/index.html")

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    pass

def tracker(request):
    pass


def productView(request):
    pass


def search(request):
    pass

def checkout(request):
    pass
