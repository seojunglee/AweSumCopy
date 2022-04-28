from rest_framework import serializers
from .models import Video, Subtitle


class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ('text','start',)