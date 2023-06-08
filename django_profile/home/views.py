from django.shortcuts import render
from django.http import HttpResponse
from .models import home
# Create your views here.

def about(request):
    homes = home.objects.all()
    return render(request,'profile.html',{'home':homes})

def contact(request):
    return HttpResponse("This is contact")
