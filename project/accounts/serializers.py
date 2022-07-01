from rest_framework import serializers
from .models import CustomUser
from accounts.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model  = CustomUser
        fields = ['id', 'first_name', 'last_name', 'country_code',
                  'country_code', 'phone_number', 'gender', 'birthdate']


class CustomUserSerializerWithToken(CustomUserSerializer):
    token        = serializers.SerializerMethodField(read_only=True)
    phone_number = serializers.SerializerMethodField(
        read_only=True, required=False)

    class Meta:
        model  = CustomUser
        fields = ['phone_number', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get__id(self, obj):
        return obj.id

    def get_phone_number(self, obj):
        return obj.phone_number
