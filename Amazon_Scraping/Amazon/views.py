from django.http.response import HttpResponse
from Amazon.models import Amazon
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def display(request):
    query_results = Amazon.objects.all()
    return render(request, 'main.html', {'obj': query_results})
