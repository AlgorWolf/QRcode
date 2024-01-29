from django.shortcuts import render
from .models import Info
# Create your views here.
 
def card(request):
    data = Info.objects.all().first()
    return render(request,"card.html",{"data":data})