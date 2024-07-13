from rest_framework import serializers
from .models import message

class Message_serializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['name', 'email', 'message']
