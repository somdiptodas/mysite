from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request):
    return JsonResponse({"msg":"success"})

def soms_code():
    print("hi")