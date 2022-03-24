from django.db import models

# Create your models here.


class MediumSummary(models.Model):
    body = models.TextField()

class LongSummary(models.Model):
    body = models.TextField()