from django.db import models
from videos.models import Video

# Create your models here.

class Quiz(models.Model):
    quiz_num = models.IntegerField(default=1)
    question = models.TextField()
    answer = models.IntegerField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)