from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
import json 
from rest_framework import status
from rest_framework.response import Response
from.import models
from rest_framework.decorators import api_view
from .serializer import Message_serializer
@api_view(["GET"])
def api_to_skills(request):
    if request.method == "GET":
        skill_list = [
            {"name": "Django"},
            {"name": "Django Rest_framework"},
            {"name": "Fastapi"},
            {"name": "sql"},
            {"name": "postgresql"}
        ]
        return Response(skill_list)
@api_view(["GET"])
def api_to_projects(request):
    if request.method=="GET":
        projects={"fastapi_project":"""User Authentication: Secure user sign-in and log-in functionality with JWT tokens.
Email Verification: Ensure user authenticity with an email verification process.
CRUD Operations: Seamlessly create, read, update, and delete posts.
Voting System: Engage with posts through an integrated voting system.
PostgreSQL Database: Robust and scalable data storage with PostgreSQL.
Beautiful Deployment: Deployed the application on Render for smooth performance and accessibility.
This project demonstrates the power and flexibility of FastAPI combined with PostgreSQL, offering a modern solution for web application development.
Check out the project: https://lnkd.in/dhvYn5kX 
Feel free to explore, give feedback, and connect with me if you’re interested in discussing more about the project or potential collaborations!""",
"django_project":"""I'm developing a robust banking system API with features for transaction management, deposits, CRUD operations for branches and banks, and customer information management. By using the django rest framework , I'm passionate about creating secure and scalable solutions that enhance financial services. Let's connect to discuss innovative tech solutions!"""}

        
        return Response(projects)
@api_view(['POST'])
def api_to_post_message(request):
    print(request.data)
    print("k",request.data)
    if request.method == 'POST':
        serializers = Message_serializer(data=request.data)
        if serializers.is_valid():
            print(request.data)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class api_to_acess_messages(generics.ListAPIView):
    queryset=models.message.objects.all()
    serializer_class=Message_serializer
    
    

    

        

