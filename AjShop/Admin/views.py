from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse ('I am Here',{})