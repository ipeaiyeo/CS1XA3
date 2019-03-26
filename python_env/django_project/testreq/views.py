from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
     return HttpResponse("Hello")
def gettest(request):
    keys = request.POST
    name = keys.get("name","")
    age = keys.get("age","")

    return HttpResponse("Hello" + name + "your" + age + "old")
# Create your views here.
