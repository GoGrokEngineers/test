from rest_framework import serializers
from .models import Competition
import random
import string


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = [
            'participants',
            'created_at',
            'six_digit_link',
            'is_active',
            'duration',
        ]

    def create(self, validated_data):
        return Competition.objects.create(**validated_data)    
    
