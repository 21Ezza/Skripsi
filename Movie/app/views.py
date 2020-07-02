from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.Controller.RecMovie import training


def training(request):
    return training().run()