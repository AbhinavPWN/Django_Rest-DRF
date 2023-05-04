from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io

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

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        #converting above data into stream 
        stream = io.BytesIO(json_data)
        #parsing stream using jsonParser
        parsed_data = JSONParser().parse(stream)
        #De-serialize (Creating serializer object)
        instance = StudentSerializer(data = parsed_data)
        if instance.is_valid():
            instance.save()
            response = {'message': 'Data inserted successfully'}
            return JsonResponse(response)
        else:
            return JsonResponse(instance.errors)
