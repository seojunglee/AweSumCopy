import imp
import re


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video, Subtitle
from .serializers import SubtitleSerializer

from videos.models import Video

# Create your views here.


@api_view(['post''get'])
def searchAPI(request, video_id):
    if video_id:

        current_video = get_object_or_404(Video, pk=video_id)
        subtitles = Subtitle.objects.filter(video = current_video).order_by('-id')
        
        q = request.POST.get('q', "")
        
        if q:
            subtitles = subtitles.filter(text__icontains=q)
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)

        #else:
            # 예외처리