from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'country_code',
                  'country_code', 'phone_number', 'gender', 'birthdate']
        extra_kwargs = {
            "errors":
                {"first_name": [{"error": "blank"}],
                 "last_name": [{"error": "blank"}],
                 "country_code": [{"error": "inclusion"}],
                 "phone_number": [{"error": "blank"}, {"error": "not_a_number"},
                                  {"error": "not_exist"},
                                  {"error": "invalid"},
                                  {"error": "taken"},
                                  {"error": "too_short", "count": 10},
                                  {"error": "too_long", "count": 15}],
                 "gender": [{"error": "inclusion"}],
                 "birthdate": [{"error": "blank"}, {"error": "in_the_future"}],
                 "avatar": [{"error": "blank"}, {"error": "invalid_content_type"}],
                 "email": [{"error": "taken"}, {"error": "invalid"}]}
        }
