from rest_framework import serializers
from .models import Video, Subtitle


class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ('text','start',)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class IDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ('id', 'videoid')