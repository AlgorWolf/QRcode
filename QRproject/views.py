from django.shortcuts import render
from .models import Info
# Create your views here.
 
def card(request,id):
    pk=1
    data = Info.objects.get(pk=id)
    return render(request,"card.html",{"data":data,"pk":pk})

def cardbio(request,id):
    pk= 0
    data = Info.objects.get(pk=id)
    return render(request,"card.html",{"data":data,"pk":pk})