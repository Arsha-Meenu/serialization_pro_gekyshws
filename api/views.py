from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# model instance/object - single student data
def student_details(request,pk):
    stu = Student.objects.get(id = pk) #complex datatype
    print(stu)
    serializer = StudentSerializer(stu)#python native datatype
    print(serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data) #json_Data
    # return HttpResponse(json_data,content_type = 'application/json'  )
    return JsonResponse(serializer.data)#instead of above commented 3 lines , we can use this jsonresponse


# queryset -all students data
def student_list(request):
    stu = Student.objects.all() #complex datatype
    print(stu)
    serializer = StudentSerializer(stu,many =True)#python native datatype
    print(serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data) #json_Data
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=False) #instead of above commented 3 lines , we can use this jsonresponse