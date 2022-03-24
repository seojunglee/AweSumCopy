
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer



@api_view(['GET'])
def showQuiz(request):
    quizes = Quiz.objects.all()
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)