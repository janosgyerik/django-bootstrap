from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def home(request):
    return render_to_response('home.html')
    #return HttpResponse('hello')
