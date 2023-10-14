from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Product
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def getapi(request):
    cont = Product.objects.all()
    serializer = NoteSerializer(cont,many = True)
    return Response(serializer.data)
