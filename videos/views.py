import imp
import re


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video, Subtitle
from .serializers import SubtitleSerializer

from videos.models import Video



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

        else:
            return render(request, 'index.html')
