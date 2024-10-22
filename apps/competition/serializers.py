from rest_framework import serializers


DIFFICULTY_CHOICES = {"Easy": "Easy", "Medium": "Medium", "Hard": "Hard"}
DURATION_CHOICES = {30: 30, 40: 40, 60: 60, 90: 90} 
PARTICIPANTS_NUMBER = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

class CompetitionSerializer(serializers.Serializer):
    competition_uid = serializers.CharField(read_only=True)
    results = serializers.DictField()  # Assuming results is a dictionary
    difficulty = serializers.ChoiceField(choices=DIFFICULTY_CHOICES)
    duration = serializers.ChoiceField(choices=DURATION_CHOICES)
    participants = serializers.ChoiceField(choices=PARTICIPANTS_NUMBER)
    created_at = serializers.DateTimeField(read_only=True)  # Assuming created_at is a timestamp
