from dataclasses import field
import imp
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('quiz_num','question', 'answer')
        