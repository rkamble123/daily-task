from rest_framework import serializers
from .models import studentModel

class studentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

def create(self,validate_data):
    return studentModel.objects.create(**validate_data)
