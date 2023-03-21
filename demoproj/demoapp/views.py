from django.shortcuts import render
from django.http import HttpResponse

#create your views here.

def index(request):
    return  render (request, 'index.html')
def name(request):
    name = request.POST['name']
    return  render (request, 'name.html',{'name':name})
    

    