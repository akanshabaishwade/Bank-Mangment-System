from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone_number', 'date_of_birth', 'tax_id', 'address', 'country', 'government_issued_id', 'customer_type', 'occupation', 'employer', 'communication_preferences', 'user_type', 'is_staff', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_active'] = True 
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return super().get_token(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)


        return data
    



