from rest_framework import serializers
from django.contrib.auth.models import User
from customer.models import Customer

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True, required=False)
    address = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone', 'address')

    def create(self, validated_data):
        phone = validated_data.pop('phone', '')
        address = validated_data.pop('address', '')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],  
            password=validated_data['password']
        )
       
        Customer.objects.create(name=user, phone_number=phone, address=address)
        return user