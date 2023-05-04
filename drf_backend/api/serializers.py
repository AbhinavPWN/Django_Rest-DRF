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
    
    def update(self,instance , validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.address = validated_data.get('address',instance.address)
        instance.qualification = validated_data.get('qualification',instance.qualification)
        instance.save()
        return instance