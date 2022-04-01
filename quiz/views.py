
import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
from django.shortcuts import get_object_or_404

from videos.models import Video
from summary.models import LongSummary



@api_view(['GET'])
def showQuiz(request, video_id):
    #퀴즈생성부
    this_quiz = Quiz()

    bert = get_object_or_404(LongSummary, pk=video_id)
    text = bert.body

    
    
    #퀴즈보여주는부분
    current_video = get_object_or_404(Video, pk=video_id)
    quizes = Quiz.objects.filter(video = current_video)
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)