from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse


# Create your views here.

# Model object -- Single object
def student_info(request,pk):
    instance = Student.objects.get(id = pk)
    data = StudentSerializer(instance).data
    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data, content_type = 'application/json')
    return JsonResponse(data)

#query Sets - all students data
def student_list(request):
    instance = Student.objects.all()
    data = StudentSerializer(instance , many= True).data
    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data,content_type = 'application/json')
    return JsonResponse(data,safe=False)