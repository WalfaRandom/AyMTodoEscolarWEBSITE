from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'aym/index.html')

def login(request):
    return render(request, 'aym/login.html')

def tables(request):
    return render(request, 'aym/tables.html')
