from rest_framework import serializers
from .models import MediumSummary, LongSummary


class MSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumSummary
        fields = ('body',)

class LSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LongSummary
        fields = ('body',)

