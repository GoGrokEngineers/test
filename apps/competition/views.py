from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Competition
from .serializers import CompetitionSerializer, TaskSerializer
from apps.task.models import Task

import random


# Create your views here.

class CompetitionCreateView(generics.CreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        competition = serializer.save() 

        difficulty = request.data.get('difficulty')
        tasks = Task.objects.filter(difficulty=difficulty)

        if not tasks.exists():
            return Response({'error': 'No tasks available for the selected difficulty'}, status=status.HTTP_400_BAD_REQUEST)

        # Randomly assign a task from the filtered tasks
        task = random.choice(tasks)

        competition = serializer.save(task=task)  # Save competition with the assigned task
        return Response({
            'id': competition.id,
            'link': competition.six_digit_link,
            'task': TaskSerializer(competition.task).data,
            'duration': competition.duration_minutes,
            'message': 'Competition created successfully!'
        }, status=status.HTTP_201_CREATED)
    

class CompetitionListView(generics.ListAPIView):
    queryset = Competition.objects.all()  
    serializer_class = CompetitionSerializer 

    

