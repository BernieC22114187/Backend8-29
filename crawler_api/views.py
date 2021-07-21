from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crawler_api.serializer import MenuSerializer
from TASBackend.models import dailyMenu

from mongoengine.errors import ValidationError


@api_view(['POST'])
def storeDailyMenu(request):
    data = JSONParser().parse(request)
    restName = data.get("RestName")
    main = data.get("Main")
    date = data.get("Date")
    side = data.get("Side")
    fruit = data.get("Fruit")
    
    if main is None:
        msg = {'message': 'body parameter "Main" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if restName is None:
        msg = {'message': 'body parameter "RestName" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if date is None:
        msg = {'message': 'body parameter "Date" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if side is None:
        msg = {'message': 'body parameter "Side" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if fruit is None:
        msg = {'message': 'body parameter "Fruit" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)    
    
    # serializer makes sure input data is changed to readable type
    serializer = MenuSerializer(data = { 
        'Main': main,
        'RestName': restName,
        'Date': date,
        'Side': side,
        'Fruit': fruit,
        
    }) 
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

# @api_view(['PUT', 'GET', 'DELETE'])
# def dish_id(request, menu_id):
#     if request.method == 'GET':
#         return get_Menu(request, menu_id)
#     elif request.method == 'PUT':
#         return update_dish(request, menu_id)
#     elif request.method == 'DELETE':
#         return delete_dish(request, menu_id)
@api_view(['GET'])
def menu_id(request, date):
    if request.method == 'GET':
        return get_Menu(request, date)
    


def get_Menu(request, date):   
    try: 
        menus = dailyMenu.objects.get(Date = date)
        
    except dailyMenu.DoesNotExist:
        return JsonResponse(
            {'message': 'menu is not in database.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'menu does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )

    serializer = MenuSerializer(menus)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )

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
        
@api_view(['PUT'])
def update_menu(request, menu_date):   
    data = JSONParser().parse(request)
    try: 
        menu = dailyMenu.objects.get(Date = menu_date)
    except dailyMenu.DoesNotExist:
        return JsonResponse(
            
            {'message': 'menu does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'menu does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = MenuSerializer(menu, data = data) # overrides the previous data

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

