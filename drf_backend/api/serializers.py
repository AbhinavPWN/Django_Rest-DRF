from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=150)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    qualification = serializers.CharField(max_length=50)
