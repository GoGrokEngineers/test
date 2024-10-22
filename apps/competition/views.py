from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from apps.competition.utils.generate_uid import generator 
from .serializers import CompetitionSerializer
from django.utils import timezone


competitions_list = []
class CompetitionCreateView(APIView):

    def get(self, request):

        # Serialize all competitions
        serialized_data = CompetitionSerializer(competitions_list, many=True).data

        return Response({
            "success": True,
            "competitions": serialized_data,
            "message": "Competitions retrieved successfully."
        }, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            # Generate a unique ID for the competition
            competition_uid = generator()

            
            competition_data = {
                "competition_uid": competition_uid,
                **serializer.validated_data,  
                "created_at": timezone.now(),
            }

            # Store the competition data in Redis cache
            cache.set(competition_uid, competition_data, timeout=competition_data["duration"] * 60)

            competitions_list.append(competition_data)

            return Response({
                "success": True,
                "competition_uid": competition_uid,
                "message": "Competition created successfully."
            }, status=status.HTTP_201_CREATED)

        
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


class JoinAPIView(APIView):
    def post(self, request):
        competion = cache.get(request.data.get("competion_uid"))
        if len(competion["participants"]) > competion["capacity"]:
            return Response({"success": False, "error": f"Competion already full filled!"}, status=status.HTTP_400_BAD_REQUEST)

        user_uid = request.data.get("user_uid")
        #loading
    

        