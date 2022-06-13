from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields =['id', 'email','username', 'password']
        extra_kwargs ={
            'password': {'write_only' : True},
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )