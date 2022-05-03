from __future__ import unicode_literals
import re
import urllib.parse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from youtube_transcript_api import YouTubeTranscriptApi
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from .models import Video, Subtitle
from .serializers import SubtitleSerializer
from .serializers import VideoSerializer
from .utils.video_info import video_id, video_subtitles, custom_subtitles
from videos.models import Video

<<<<<<< HEAD
# import youtube_dl
# import pandas as pd
# from time import sleep
# import os
# from selenium import webdriver # for interacting with website

=======
>>>>>>> yuna


def index(request):

    current_video = get_object_or_404(Video, pk=6) #pk임시고정
    return render(request, 'index.html',{'video': current_video})


@api_view(['POST','GET'])
def searchAPI(request, video_id):

    if video_id:
        current_video = get_object_or_404(Video, pk=video_id)
        subtitles = Subtitle.objects.filter(video = current_video)

        q = request.POST.get('q', "")
        
        if q: 
            subtitles = subtitles.filter(text__icontains=q)
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)

<<<<<<< HEAD
        #else:
            # 예외처리




@api_view(['POST'])
def saveVideo(request):
    if request.method == 'POST':
        url = request.data.get("url", "")
        if url:
            vid = video_id(url)
            texts = video_subtitles(vid)
            transcripts = custom_subtitles(vid)
            check_vid = Video.objects.filter(videoid=vid)
            if not check_vid:
                video = Video(videoid=vid, transcript=texts)
                video.save()
                for transcript in transcripts:
                    subtitle = Subtitle(videoid=video, text=transcript['text'], start=transcript['start'])
                    subtitle.save()
                return Response(status=200, data='inserted successfully')
            else:
                video = Video.objects.get(videoid=vid)
                video.transcript = texts
                video.save()
                pk = video.id
                subtitles = Subtitle.objects.filter(videoid=pk)
                subtitles.delete()
                for transcript in transcripts:
                    subtitle = Subtitle(videoid=video, text=transcript['text'], start=transcript['start'])
                    subtitle.save()
                return Response(status=200, data='updated succesfully')
    else:
        return Response(status=405, data='Method Not Allowed')



# @api_view(['GET'])
# def streamVideo(request):
#     serializer = VideoSerializer()
#     return Response("")
=======
        else:
            return render(request, 'index.html')
>>>>>>> yuna
