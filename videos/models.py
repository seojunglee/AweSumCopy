from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    videoid = models.CharField(max_length=50)
    transcript = models.TextField()
    
class Subtitle(models.Model):
    text = models.TextField()
    start = models.FloatField()

    
