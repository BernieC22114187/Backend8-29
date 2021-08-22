from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from exercise_api.serializer import ExerciseSerializer
from TASBackend.models import exercise
from mongoengine.errors import ValidationError

    

@api_view(['GET'])

def get_exercise(request, exercise_name):   
    try:
        item = exercise.objects.get(Name = exercise_name)
    except:
        return JsonResponse(
            
            {"message": "exercise does not exist"} ,
            status = status.HTTP_404_NOT_FOUND
            
        )
    serializer = ExerciseSerializer(item)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )
    

