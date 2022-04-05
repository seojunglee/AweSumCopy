import imp
import re


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from summarizer.sbert import SBertSummarizer


from transformers import pipeline





from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MediumSummary, LongSummary
from .serializers import MSummarySerializer, LSummarySerializer

from videos.models import Video


### LONG SUMMARY

@api_view(['get'])
def showLongAPI(request, video_id):
    if video_id:
        #요약 생성부
        model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
        l_summary = LongSummary() #객체 생성

        this_video = get_object_or_404(Video, pk=video_id)
        text = this_video.transcript    #텍스트 가져오기

        l_summary.body = model(text, num_sentences=15)      #요약문 generate
    
        l_summary.video = this_video
        l_summary.save()  #저장 

        #해당 영상에 대한 summary 필터링 후 전달
        current_video = get_object_or_404(Video, pk=video_id)
        l_summary = LongSummary.objects.filter(video = current_video)

        serializer = LSummarySerializer(l_summary, many=True)
        return Response(serializer.data)









### MEDIUM SUMMARY 
@api_view(['get'])
def showMediumAPI(request, video_id):

    m_summary = MediumSummary()  #객체생성
    
    #요약 생성(long 불러와서 생성요약하기) 
    current_video = get_object_or_404(Video, pk=video_id)
    l_summary = LongSummary.objects.filter(video = current_video)[0]



    
    

    m_summary.body = l_summary.body

    m_summary.video = l_summary.video
    m_summary.save()  #저장 



    #요약 전달
    current_video = get_object_or_404(Video, pk=video_id)
    m_summary = MediumSummary.objects.filter(video = current_video)

    serializer = MSummarySerializer(m_summary, many=True)
    return Response(serializer.data)
