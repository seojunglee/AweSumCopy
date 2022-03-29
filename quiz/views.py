
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer



@api_view(['GET'])
def showQuiz(request):
    #퀴즈생성부

    
    #퀴즈보여주는부분
    quizes = Quiz.objects.all()
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)