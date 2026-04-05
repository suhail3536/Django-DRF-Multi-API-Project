from django.shortcuts import render
from django.http import JsonResponse

def students(request):
    students={
        'id':1,
        'name':'suhail1',
        'class':'CSE'
    }
    return JsonResponse(students)
