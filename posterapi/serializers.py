from rest_framework.serializers import ModelSerializer
from .models import Product
from rest_framework import serializers



class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
