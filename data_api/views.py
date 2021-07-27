from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from data_api.serializer import DataSerializer
from TASBackend.models import data
from mongoengine.errors import ValidationError
from TASBackend.models import dish


@api_view(['GET', 'POST'])
def func(request, member_id, timestamp):
    if request.method == 'GET':
        return getMemberNutrition(request, member_id, timestamp)
    elif request.method == 'POST':
        return storeMemberNutrition(request, member_id, timestamp)


def getMemberNutrition(request, member_id, timestamp): 
    # gets today's member nutrition data
    # print("timestamp: ", timestamp)
    member_filter = {}
    member_filter = {'Member_id': member_id, 'Timestamp': str(timestamp)} 
    print(member_filter)
    try:
        curMember = data.objects.get(__raw__ = member_filter)
        # print("curMemberID: ", curMember.id)

    except data.DoesNotExist:
         return JsonResponse(
            {'message': 'Member has no data yet'},
            status = status.HTTP_200_OK
        )

    except ValidationError:
        return JsonResponse(
            {'message': 'Member does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = DataSerializer(curMember)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )

def storeMemberNutrition(request, member_id, timestamp): # store nutrition based on list of dishes
    timestamp = str(timestamp)
    request_data = JSONParser().parse(request)
    dishList = request_data['dishList']
    
    print(dishList)
    if dishList is None:
        msg = {'message': 'body parameter "Data" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
 
    cal = 0;  carb = 0;  prot = 0;  fat = 0;  chol = 0; sod = 0;  

    for dishName in dishList:
        Dish = dish.objects.get(Name = dishName)
        cal+= Dish.Calories; carb+= Dish.Total_Carbs; prot+= Dish.Protein; fat+= Dish.Total_Fat; chol+= Dish.Cholesterol; sod+= Dish.Sodium; 
    
    
    member_filter = {'Member_id': member_id, 'Timestamp': timestamp} 
    
    try: 
        curMember = data.objects.get(__raw__ = member_filter)
        curMember["Calories"] += cal
        curMember["Total_Fat"] += fat
        curMember["Cholesterol"] += chol
        curMember["Sodium"] += sod
        curMember["Total_Carbs"] += carb
        curMember["Protein"] += prot

        serializer = DataSerializer( curMember, data = { 
            'Member_id': member_id,
            'Timestamp': timestamp,
            'Calories': curMember["Calories"],
            'Total_Fat': curMember["Total_Fat"],
            'Cholesterol': curMember["Cholesterol"],
            'Sodium': curMember["Sodium"],
            'Total_Carbs': curMember["Total_Carbs"],
            'Protein': curMember["Protein"],


        }  ) 
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe = False, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    except data.DoesNotExist: # when user has not entered dishes/nutrition info today ==> no need to add on
        serializer = DataSerializer(data = { 
            'Member_id': member_id,
            'Timestamp': timestamp,
            'Calories': cal, 
            'Total_Fat': fat,
            'Cholesterol': chol,
            'Sodium': sod,
            'Total_Carbs': carb,
            'Protein': prot,
            
        }) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

