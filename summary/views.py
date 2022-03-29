
import imp
import re

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from summarizer import Summarizer as BERT

from transformers import pipeline


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MediumSummary, LongSummary
from .serializers import MSummarySerializer, LSummarySerializer

from videos.models import Video


# 테스트용!!!!!!!
import spacy
def summarize(request):   #predictMPG
    if request.method == 'POST':
        temp={}
        temp['text'] = request.POST.get('textValue')
    body = temp['text']
    #result = reloadModel(body, min_length=60)
    #ans = ''.join(result)
    model = BERT()  #원래 Summarizer였음
    result = model(body, min_length=60)
    ans = ''.join(result)
    ##context = {'ans': ans}
    return render(request, 'index.html', ans)




### MEDIUM SUMMARY - 미완성..!
@api_view(['get'])
def showMediumAPI(request, video_id):
    #요약 생성(long 불러와서 생성요약하기)
    l_summary = get_object_or_404(LongSummary, pk=video_id)

    #요약 전달
    m_summary = MediumSummary.objects.all()
    serializer = MSummarySerializer(m_summary, many=True)
    return Response(serializer.data)




### LONG SUMMARY

@api_view(['get'])
def showLongAPI(request, video_id):
    if video_id:
        #요약 생성
        model = BERT()
        l_summary = LongSummary()

        this_video = get_object_or_404(Video, pk=video_id)
        text = this_video.transcript #텍스트 가져오기

        l_summary.body = model(text, min_length=60) #요약문 generate
        l_summary.save()  #저장 


        #요약 전달
        l_summary = get_object_or_404(LongSummary, pk=video_id)
        serializer = LSummarySerializer(l_summary, many=True)
        return Response(serializer.data)
