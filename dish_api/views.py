from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dish_api.serializer import DishSerializer
from TASBackend.models import dish
from mongoengine.errors import ValidationError



@api_view(['POST'])
def storeNutrition(request):
    data = JSONParser().parse(request)
    dishName = data.get("Name")
    totalcal = data.get("Calories")
    totalFat = data.get("Total Fat")
    cholesterol = data.get("Cholesterol")
    sodium = data.get("Sodium")
    totalCarbs = data.get("Total Carbs")

    protein = data.get("Protein")
    index = data.get("Index") 
    timestamp = data.get("Timestamp")
    
    if dishName is None:
        msg = {'message': 'body parameter "Name" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if totalcal is None:
        msg = {'message': 'body parameter "Calories" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if totalFat is None:
        totalFat = 0
    if cholesterol is None:
        cholesterol = 0
    if sodium is None:
        sodium = 0
    if totalCarbs is None:
        totalCarbs = 0
    if protein is None:
        protein = 0
    
    # serializer makes sure input data is changed to readable type
    serializer = DishSerializer(data = { 
        'Name':dishName,
        'Calories': totalcal,
        'Total_Fat': totalFat,
        'Cholesterol': cholesterol,
        'Sodium': sodium,
        'Total_Carbs' : totalCarbs,
        'Protein': protein,
        'Index': index,
        'Timestamp': timestamp,
    }) 
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'GET', 'DELETE'])
def dish_id(request, dish_id):
    if request.method == 'GET':
        return get_dish(request, dish_id)
    elif request.method == 'PUT':
        return update_dish(request, dish_id)
    elif request.method == 'DELETE':
        return delete_dish(request, dish_id)

def get_dish(request, dish_id):   
    
    serializer = DishSerializer()
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )
#     try: 
#         dish = dish.objects.get(id = dish_id)
#     except dish.DoesNotExist:
#         return JsonResponse(
#             {'message': 'dish is not in database.'},
#             status = status.status.HTTP_400_NOT_FOUND
#         )
#     except ValidationError:
#         return JsonResponse(
#             {'message': 'dish does not exist'},
#             status = status.HTTP_404_NOT_FOUND
#         )

#     serializer = DishSerializer(dish)
#     return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )
@api_view(['GET'])
def input_filtDish(request, index, timestamp):

    dish_filter = {}
    if index != '':

        dish_filter['Index'] = int(index)
    if timestamp != '':
    
        dish_filter["Timestamp"] = {'$gte': int(timestamp), '$lte': int(timestamp)+604800} # seconds per week

    dishes = dish.objects(__raw__ = dish_filter)
    dish_serializer = DishSerializer(dishes, many=True)
    return JsonResponse(dish_serializer.data, safe=False)

# def get_filteredDish(request, dishName, index, timestamp):
#     data = JSONParser().parse(request)
#     try: 
#         dishesInCaf = dish.objects.filter(id = index)
#         print(dishesInCaf)
#         dish = dishesInCaf.objects.get(Name = dishName)
#     except dish.DoesNotExist:
#         return JsonResponse(
            
#             {'message': 'dish does not exist.'},
#             status = status.status.HTTP_400_NOT_FOUND
#         )
        

def update_dish(request, dish_id):   
    data = JSONParser().parse(request)
    try: 
        tempDish = dish.objects.get(id = dish_id)
    except dish.DoesNotExist:
        return JsonResponse(
            
            {'message': 'dish does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )

    except ValidationError:
        return JsonResponse(
            {'message': 'dish does not exist'},
            status = status.HTTP_404_NOT_FOUND
            
        )
    serializer = DishSerializer(tempDish, data = data) # overrides the previous data

    if serializer.is_valid():
        
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def delete_dish(request, dish_id):
    try: 
        tempDish = dish.objects.get(id = dish_id)
    except dish.DoesNotExist:
        return JsonResponse(
            {'message': 'dish does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'dish does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )

    dish.delete()
    return JsonResponse({'message': 'dish deleted successfully'}, status = status.HTTP_200_OK)

