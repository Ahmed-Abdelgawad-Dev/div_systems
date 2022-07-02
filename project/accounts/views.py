from rest_framework.response import Response
import itertools
from .serializers import CustomUserSerializer, CustomUserSerializerWithToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


"""----------------------------------------------------------------------------------------------------------------"""
"""Task One"""
"""----------------------------------------------------------------------------------------------------------------"""
@api_view(['POST'])
@csrf_exempt
def register_user(request): 
    if request.method == 'POST':
        if request.data['password']:
            password  = make_password(request.data['password'])
        # if accepts Files =>  += {files=request.FILES} after data 
        # + input type=file multiple at html forms
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""----------------------------------------------------------------------------------------------------------------"""
"""Task Two"""
"""----------------------------------------------------------------------------------------------------------------"""
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data            = super().validate(attrs)
        serialized_user = CustomUserSerializerWithToken(self.user).data
        # Return below dict to see or return the whole response or check it in terminal.
        print('Object: =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', dict(
            itertools.islice(serialized_user.items(), 2)))
        return serialized_user['token']


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

"""----------------------------------------------------------------------------------------------------------------"""
"""Task Three"""
"""----------------------------------------------------------------------------------------------------------------"""


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def phone_token_login(request):
        # if request.method=="POST":
            
        # if request.user.is_authenticated:
        #     data={}
        #     first_name=request.
        # serializer = CustomUserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass