from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
#create your views here.

def index(request):
    products = Product.objects.all()
    return  render (request, 'index.html',{'products':products})
def name(request):
    name = request.POST['name']
    return  render (request, 'name.html',{'name':name})
    

    