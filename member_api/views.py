from rest_framework.decorators import api_view
from rest_framework import status 

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from member_api.serializer import MemberSerializer
from TASBackend.models import Member
from mongoengine.errors import ValidationError

@api_view(['POST'])
def storeNutrition(request):
    data = JSONParser().parse(request)
    totalcal = data.get("Calories")
    totalFat = data.get("Total Fat")
    cholesterol = data.get("Cholesterol")
    sodium = data.get("Sodium")
    totalCarbs = data.get("Total Carbs")
    protein = data.get("Protein")  

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
    serializer = MemberSerializer(data = { 
        'Calories': totalcal,
        'Total Fat': totalFat,
        'Cholesterol': cholesterol,
        'Sodium': sodium,
        'Total Carbs' : totalCarbs,
        'Protein': protein,
    }) 
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    account = data.get("account")
    password = data.get("password")
    height = data.get("height")
    weight = data.get("weight")


    if account is None:
        msg = {'message': 'body parameter "account" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if password is None:
        msg = {'message': 'body parameter "password" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)

    if weight is None:
        msg = {'message': 'body parameter "weight" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)

    if height is None:
        msg = {'message': 'body parameter "height" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    
    # serializer makes sure input data is changed to readable type
    serializer = MemberSerializer(data = { 
        'account': account,
        'password': password,
        'weight': weight,
        'height': height
    }) 
    #big parenthesis becuase it is a JSON
    
    if serializer.is_valid():
        try: 
            
            Member.objects.get(account = account)
        except Member.DoesNotExist:
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
            
        return JsonResponse({"message":"user already exists"}, status = status.HTTP_400_BAD_REQUEST)  

    return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request) #reads the file / converts, like dictionary
    account = data.get("account")
    password = data.get("password")
    
    if account is None: # detects if account is given
        msg = {'message': 'body parameter "account" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)
    if password is None:
        msg = {'message': 'body parameter "password" should be given' }
        return JsonResponse(msg, status= status.HTTP_400_BAD_REQUEST)

    try: 
        user = Member.objects.get(account = account)

    except Member.DoesNotExist:
        return JsonResponse(
            {'message': 'user does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    if user.password == password:
        serializer = MemberSerializer(user)
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)

    return JsonResponse({'message': 'account or password incorrect'}, # password incorrect
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['PUT', 'GET', 'DELETE'])
def member_id(request, user_id):
    if request.method == 'GET':
        return get_member(request, user_id)
    elif request.method == 'PUT':
        return update_member(request, user_id)
    elif request.method == 'DELETE':
        return delete_member(request, user_id)

def get_member(request, user_id):   
    try: 
        user = Member.objects.get(id = user_id)
    except Member.DoesNotExist:
        return JsonResponse(
            {'message': 'user does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'User does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )

    serializer = MemberSerializer(user)
    return JsonResponse(serializer.data, status = status.HTTP_200_OK, safe = False )

def update_member(request, user_id):   
    data = JSONParser().parse(request)
    try: 
        user = Member.objects.get(id = user_id)
    except Member.DoesNotExist:
        return JsonResponse(
            
            {'message': 'user does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'User does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )
    serializer = MemberSerializer(user, data = data) # overrides the previous data

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def delete_member(request, user_id):
    try: 
        user = Member.objects.get(id = user_id)
    except Member.DoesNotExist:
        return JsonResponse(
            {'message': 'user does not exist.'},
            status = status.HTTP_404_NOT_FOUND
        )
    except ValidationError:
        return JsonResponse(
            {'message': 'User does not exist'},
            status = status.HTTP_404_NOT_FOUND
        )

    user.delete()
    return JsonResponse({'message': 'User deleted successfully'}, status = status.HTTP_200_OK)