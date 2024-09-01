from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd


def preQuestions(request):

    #df = pd.read_csv( "./questions/preQuestionData.csv" )
    return HttpResponse("Hello, world. You're at the pre-ques index.%s"%request.content_params)
