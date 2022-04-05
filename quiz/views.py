
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
    current_video = get_object_or_404(Video, pk=video_id)
    bert = LongSummary.objects.filter(video = current_video)[0]
    
    text = bert.body
    list = text.split('.')

    
    for i, each_line in enumerate(list):
        this_quiz = Quiz()
        if i%2 == 0:
            this_quiz.question = "True Ex" + each_line
            this_quiz.answer = 1
            
        else:
            this_quiz.question = "False Ex" + each_line
            this_quiz.answer = 0

        this_quiz.video = bert.video
        if i != len(list)-1 :
            this_quiz.save()
        i+=1


        


    
    
    #퀴즈보여주는부분
    current_video = get_object_or_404(Video, pk=video_id)
    quizes = Quiz.objects.filter(video = current_video)
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)