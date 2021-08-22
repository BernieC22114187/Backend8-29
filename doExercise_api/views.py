from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from doExercise_api.serializer import doExerciseSerializer
from data_api.serializer import DataSerializer
from TASBackend.models import doExercise
from mongoengine.errors import ValidationError
from TASBackend.models import exercise
from TASBackend.models import data
from TASBackend.models import Member

@api_view(['GET'])


def getMemberExercise(request, member_id, timestamp): 
    
    member_filter = {}
    member_filter = {'Member_id': member_id, 'Timestamp': str(timestamp)} 
    print(member_filter)
    try:
        curMember = doExercise.objects.get(__raw__ = member_filter)
        

    except doExercise.DoesNotExist:
         return JsonResponse(
            {'message': 'Member has no data yet'},
            status = status.HTTP_200_OK
        )
    
    except ValidationError:
        return JsonResponse(
            {'message': 'Member does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = doExerciseSerializer(curMember)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )

@api_view(['POST'])

def storeMemberExercise(request, member_id, timestamp, duration): # store exercise based on list of dishes
    timestamp = str(timestamp)
    duration = float(duration)
    request_data = JSONParser().parse(request)
    exerciseItem = request_data['exerciseItem']
    
    print(exerciseItem)
    if exerciseItem is None:
        msg = {'message': 'body parameter "exerciseItem" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    
    cal = 0    
    
    member_filter = {'Member_id': member_id, 'Timestamp': timestamp} 
    
    try: 
        
        curMemberData = data.objects.get(__raw__ = member_filter)
        curMember = Member.objects.get(id = member_id)
        
        
        item = exercise.objects.get(Name = exerciseItem)
        cal+= item.Ratio * curMember.weight * (duration / 60)
        
        
        if curMemberData["Calories"] < cal:
            return JsonResponse(
                {"message":"Not enough calories available/to burn"}, status = status.HTTP_200_OK
            )
        curMemberData["Calories"] -= cal
        serializer = DataSerializer( curMemberData, data = { 
            'Member_id': member_id,
            'Timestamp': timestamp,
            'Calories': curMemberData["Calories"],
            'Total_Fat': curMemberData["Total_Fat"],
            'Cholesterol': curMemberData["Cholesterol"],
            'Sodium': curMemberData["Sodium"],
            'Total_Carbs': curMemberData["Total_Carbs"],
            'Protein': curMemberData["Protein"],


        }  ) 
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe = False, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        


    except : 
        
        return JsonResponse({"message": "No calories available/to burn"}, status = status.HTTP_200_OK)
    

