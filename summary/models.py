from django.db import models
from videos.models import Video
# Create your models here.


class MediumSummary(models.Model):
    body = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)


class LongSummary(models.Model):
    body = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)