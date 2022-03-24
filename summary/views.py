
import imp
import re

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from summarizer import Summarizer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MediumSummary, LongSummary
from .serializers import MSummarySerializer, LSummarySerializer



#import joblib
# RFModelforMPG.pkl == SummaryModel.pkl
#reloadModel = joblib.load('./models/SummaryModel.pkl')

import spacy
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


@api_view(['get'])
def showMediumAPI(request):
    m_summary = MediumSummary.objects.all()
    serializer = MSummarySerializer(m_summary, many=True)
    return Response(serializer.data)

@api_view(['get'])
def showLongAPI(request):
    l_summary = LongSummary.objects.all()
    serializer = LSummarySerializer(l_summary, many=True)
    return Response(serializer.data)
