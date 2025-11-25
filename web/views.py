from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from web import models


# Create your views here.


def trans(request):
    return render(request, 'index.html')
