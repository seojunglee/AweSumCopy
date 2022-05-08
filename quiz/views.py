
import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
from django.shortcuts import get_object_or_404

from videos.models import Video
from summary.models import LongSummary




@api_view(['GET'])
def showQuiz(request):

    video_id = request.GET.get('id')


    #퀴즈생성부
    current_video = get_object_or_404(Video, pk=video_id)
    bert = LongSummary.objects.filter(video = current_video)[0]
    
    text = bert.body
    list = text.split('.')

    
    for i, each_line in enumerate(list):
        this_quiz = Quiz()
        if i%2 == 0: 
            this_quiz.question = "True_Ex : " + each_line
            this_quiz.answer = 1
            
        else: 
            #  < 거짓 문장으로 가공> 코드 삽입
            this_quiz.question = "False_Ex : " + each_line
            this_quiz.answer = 0

        this_quiz.video = bert.video

        if i != len(list)-1 :
            #< 문장을 퀴즈 형태로 가공 > 코드 삽입
            this_quiz.quiz_num=i+1
            this_quiz.save()
        i+=1


    
    #퀴즈보여주는부분
    quizes = Quiz.objects.filter(video = current_video)
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)