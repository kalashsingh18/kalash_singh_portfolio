from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
import json 
from rest_framework import status
from rest_framework.response import Response
from.import models
from rest_framework.decorators import api_view
from .serializer import Message_serializer,Project_serializer
@api_view(["GET", "POST"])
def api_to_skills(request):
    Skills=models.skills
    if request.method == "GET":
        try:
            instance = Skills.objects.first()  # Assuming you want to retrieve the first instance
            if instance:
                skill_list = instance.get_items()
                return Response(skill_list)
            else:
                return Response([])
        except Skills.DoesNotExist:
            return Response([])
    
    elif request.method == "POST":
        try:
            instance = Skills.objects.first()  # Assuming there's only one instance for this model
            if not instance:
                instance = Skills()

            instance.set_items(request.data.get('skills', []))
            instance.save()
            return Response({"message": "Skills updated successfully"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

class api_to_projects(generics.ListCreateAPIView):
    queryset=models.projects.objects.all()
    serializer_class=Project_serializer

    
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
    

    

        

