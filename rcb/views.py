from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def vk(request):
    return HttpResponse('<h1><marquee>the GOAT </marquee> </h1>') 
def dev(request):
    return render(request,'dev.html')