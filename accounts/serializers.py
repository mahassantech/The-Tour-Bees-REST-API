from rest_framework import serializers 
from .models import RegisterModel


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta :
        model=RegisterModel
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "profile_photo",
            "password",
        ]
    def create(self, validated_data):
        password=validated_data.pop('password')
        user=RegisterModel(**validated_data)
        user.set_password(password)
        user.save()
        return user