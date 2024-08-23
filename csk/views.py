from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return HttpResponse('hello dhoni')
def kira(request):
    return render(request,'kira.html')