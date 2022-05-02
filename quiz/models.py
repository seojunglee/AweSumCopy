from django.db import models
from videos.models import Video

# Create your models here.

class Quiz(models.Model):
    question = models.TextField()
    answer = models.IntegerField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)