
import imp

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
from django.shortcuts import get_object_or_404

from videos.models import Video
from summary.models import LongSummary

from .utils.quiz_code import *
from .utils.false_code import *

from random import *

import time

@api_view(['GET'])
def showQuiz(request):



    video_id = request.GET.get('id')

    #퀴즈생성부
    current_video = get_object_or_404(Video, pk=video_id)
    bert = LongSummary.objects.filter(video = current_video)[0]
    
    text = bert.body

    #  < 거짓 문장으로 가공>
    cand_sents = get_candidate_sents(text)
    filter_quotes_and_questions = preprocess(cand_sents)
    sent_completion_dict = get_sentence_completions(filter_quotes_and_questions)

    final = []
    for key_sentence in sent_completion_dict:
        partial_sentences = sent_completion_dict[key_sentence]
        false_sentences =[]
        ii = 2
        for partial_sent in partial_sentences:
            false_sents = generate_sentences(partial_sent,key_sentence)
            false_sentences.extend(false_sents)
            if ii == 2:
                final.extend(false_sents)
                print(false_sents)
            ii = 3


    list = text.split('.' or '?')

    temp = min(len(list), len(final))

    for i in range (temp) :
        if i%2==1:
            list[i] = final[i]


    qe= BoolQGen()
    
    for i, each_line in enumerate(list):
        this_quiz = Quiz()
        this_quiz.video = bert.video
        this_quiz.question = (qe.predict_boolq(each_line).get('Boolean Questions'))[1]
        if i%2 == 0:
            this_quiz.answer = 1
        else:
            this_quiz.answer = 0

        if i != len(list)-1 :
            this_quiz.quiz_num=i+1
            this_quiz.save()
        i+=1

    



    #퀴즈보여주는부분
    quizes = Quiz.objects.filter(video = current_video)
    serializer = QuizSerializer(quizes, many=True)

    return Response(serializer.data)
    # time.sleep(10)
    # return Response("ok")