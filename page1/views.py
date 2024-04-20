
from django.shortcuts import render

# Create your views here.
def page1_page(request):
    return render(request,'home/home.html')