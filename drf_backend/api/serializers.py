from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=150)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    qualification = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)