from rest_framework.response import Response
import itertools
from django.conf import settings
from .serializers import CustomUserSerializer, CustomUserSerializerWithToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@api_view(['GET'])
def test_view(request):
    return Response({'test_view': 'django'})


@api_view(['POST'])
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        if request.data['password']:
            password = make_password(request.data['password'])
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data            = super().validate(attrs)
        serialized_user = CustomUserSerializerWithToken(self.user).data
        print('Object: =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', dict(
            itertools.islice(serialized_user.items(), 2)))
        return serialized_user['token']


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
