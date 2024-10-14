from rest_framework import serializers
from .models import Competition
import random
import string
from apps.task.serializers import TaskSerializer


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        task = TaskSerializer(read_only=True)
        model = Competition
        fields = [
            'participants',
            'difficulty',
            'created_at',
            'six_digit_link',
            'is_active',
            'duration',
        ]

    def create(self, validated_data):
        return Competition.objects.create(**validated_data)    
    
