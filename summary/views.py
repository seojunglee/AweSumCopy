
import imp
import re

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from summarizer import Summarizer
# Create your views here.

import spacy

#import joblib
# RFModelforMPG.pkl == SummaryModel.pkl
#reloadModel = joblib.load('./models/SummaryModel.pkl')


def index(request):
    context = {'a': 'HelloWorld'}
    return render(request, 'index.html',context)


def summarize(request):   #predictMPG
    if request.method == 'POST':
        temp={}
        temp['text'] = request.POST.get('textValue')
    body = temp['text']
    #result = reloadModel(body, min_length=60)
    #ans = ''.join(result)
    model = Summarizer()
    result = model(body, min_length=60)
    ans = ''.join(result)
    context = {'ans': ans}
    return render(request, 'index.html',context)