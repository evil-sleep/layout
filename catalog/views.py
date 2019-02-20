from django.shortcuts import render
from django.http import HttpResponse


def index_response(request):
    return HttpResponse('<h2>health check</h2>')


def index(request):
    return render(request, 'catalog/homepage.html')

