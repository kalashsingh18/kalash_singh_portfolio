from rest_framework import serializers
from .models import message,projects

class Message_serializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['name', 'email', 'message']
class Project_serializer(serializers.ModelSerializer):
    class Meta:
        model=projects
        fields=['project_name',"project_description"]
