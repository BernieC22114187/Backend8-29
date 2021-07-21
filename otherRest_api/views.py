from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from otherRest_api.serializer import constMenuSerializer
from TASBackend.models import constantMenu
from mongoengine.errors import ValidationError



@api_view(['POST'])
def storeConstMenu(request):
    data = JSONParser().parse(request)
    restName = data.get("RestName")
    menu = data.get("Menu")
    date = data.get("Date")
    
    if menu is None:
        msg = {'message': 'body parameter "Menu" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if restName is None:
        msg = {'message': 'body parameter "RestName" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if date is None:
        msg = {'message': 'body parameter "Date" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)

    
    # serializer makes sure input data is changed to readable type
    serializer = constMenuSerializer(data = { 
        'Menu': menu,
        'RestName': restName,
        'Date': date,
        
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

def get_Menu(request, restName):   
    '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
    try:     
        # restName = request.GET.get('restName', None)
        # if restName is not None:
        menus = constantMenu.objects.get()
           
        # else:
        # return JsonResponse(
        #     {'message': 'restName does not exist'},
        #     status = status.HTTP_404_NOT_FOUND
        # )
    except constantMenu.DoesNotExist:
        return JsonResponse(
            {'message': 'menu is not in database.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'menu does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )

    serializer = constMenuSerializer(menus)
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
def update_menu(request, name):   
    data = JSONParser().parse(request)
    try: 
        menu = constantMenu.objects.get(RestName = name)
    except constantMenu.DoesNotExist:
        return JsonResponse(
            
            {'message': 'menu does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'menu does not exist'},
            
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = constMenuSerializer(menu, data = data) # overrides the previous data

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

