from django.db import models


class Video(models.Model):
    videoid = models.CharField(max_length=50, unique=True)
    transcript = models.TextField()


class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    start = models.TextField()