import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from utils.generate_uid import generator 

class CompetitionCreateView(APIView):
    def post(self, request):
        DIFFICULTY_CHOICES = {"Easy": "Easy", "Medium": "Medium", "Hard": "Hard"}
        DURATION_CHOICES = {30: 30, 40: 40, 60: 60, 90: 90} 

        try:
            difficulty = DIFFICULTY_CHOICES[request.data.get("difficulty")]
            duration = DURATION_CHOICES[request.data.get("duration")]
            capacity = request.data.get("duration")

            competition_uid = generator()

            competition_data = {
                "participants": {},
                "results": {},
                "difficulty": difficulty,
                "duration": duration,
                "capacity": capacity,
                "created_at": time.time(),
            }

            cache.set(competition_uid, competition_data, timeout=duration*60)

            return Response({
                "success": True,
                "competition_uid": competition_uid,
                "message": "Competition created successfully."
            }, status=status.HTTP_201_CREATED)

        except KeyError as ex:
            return Response({"success": False, "error": f"Invalid value: {str(ex)}"}, status=status.HTTP_400_BAD_REQUEST)


class JoinAPIView(APIView):
    def post(self, request):
        competion = cache.get(request.data.get("competion_uid"))
        if len(competion["participants"]) > competion["capacity"]:
            return Response({"success": False, "error": f"Competion already full filled!"}, status=status.HTTP_400_BAD_REQUEST)

        user_uid = request.data.get("user_uid")
        #loading
    

        