from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rs(request):
    return HttpResponse('rs captain')
def kavitha(request):
    return render(request,'kavitha.html')


