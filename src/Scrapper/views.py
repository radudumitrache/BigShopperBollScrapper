from django.shortcuts import render,redirect
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request) :
    return HttpResponse("Hello world")