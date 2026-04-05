from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students=[
        {'id':1,'name':'suhail','age':25}
    ]
    return HttpResponse('<h2> hellow world</h2>')

