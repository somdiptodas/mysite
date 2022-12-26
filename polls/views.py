from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

from django.http import HttpResponse,  JsonResponse


@csrf_exempt
def index(request):
    print(request.method)
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods
@csrf_exempt
def new_sss(request):
   if request.method != "GET":
       return JsonResponse({"msg":"Failed"}, status = 405)
   return HttpResponse("SSS function excuited.")