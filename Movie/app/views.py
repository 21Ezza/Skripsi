from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.Controller.RecMovie import Training

import os


def trainingData(request):
    if request.method == "GET":
        result = Training().run(os.path.join(os.path.dirname(os.path.dirname(__file__)),'input/movies.csv'))
    return HttpResponse(result);