from rest_framework import serializers
from.models import *

class ContactNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        fields = "__all__"

class SignUpSerializer(serializers.ModelSerializer):
    number = ContactNumberSerializer(many=False)
    class Meta:
        model = Signup
        fields = ('id', 'first_name', 'last_name', 'number', 'email', 'dob')
    '''
    def create(self, validated_data):
        number = ContactNumber.objects.get(pk=validated_data.pop('event')
        sign = Signup.objects.create(**validated_data)
        return sign

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
    '''
