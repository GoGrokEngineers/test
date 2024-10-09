from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Competition
from .serializers import CompetitionSerializer

# Create your views here.

class CompetitionCreateView(generics.CreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        competition = serializer.save() 
        return Response({
            'id': competition.id,
            "link" : competition.six_digit_link,
            'message': 'Competition created successfully!'
        }, status=status.HTTP_201_CREATED)
    
    
class CompetitionListView(generics.ListAPIView):
    queryset = Competition.objects.all()  
    serializer_class = CompetitionSerializer 


