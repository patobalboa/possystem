from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def baseUrl(request):
    return render(request, 'core/body.html')