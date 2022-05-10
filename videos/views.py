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
from .serializers import IDSerializer, SubtitleSerializer
from .serializers import VideoSerializer
from .utils.video_info import video_id, video_subtitles, custom_subtitles
from videos.models import Video




def index(request):

    current_video = get_object_or_404(Video, pk=13) #pk임시고정
    return render(request, 'index.html',{'videoid': current_video})




@api_view(['GET'])
def searchAPI(request):
    if request.query_params:
        video_id = request.query_params.get('id', None)
        q = request.query_params.get('q', None)
        current_video = get_object_or_404(Video, pk=video_id)
        subtitles = Subtitle.objects.filter(videoid = current_video)

        if q:
            subtitles = subtitles.filter(text__icontains=q)
            val = 1
            for i in subtitles:
                i.sub_num = val
                val = val + 1
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)

        else:
            return Response(status=405, data='Method Not Allowed')



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
                    serializer = IDSerializer(video)
                return Response(serializer.data, status=200)
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
                serializer = IDSerializer(video)
                return Response(serializer.data, status=200)
    else:
        return Response(status=405, data='Method Not Allowed')


