from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime, timedelta

def sample(request):
    return JsonResponse({"Done":"Done"},safe=False)  