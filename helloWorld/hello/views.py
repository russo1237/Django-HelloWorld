from django.shortcuts import render
from .models import message
# Create your views here.
def index(request):
    msg = {
        "message" : message.objects.first()
    }
    return render(request,"hello/index.html",msg)