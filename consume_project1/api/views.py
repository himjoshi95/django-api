from django.shortcuts import render
from .models import Student ,Teacher
from .serializers import StudentSerializer , TeacherSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

def studentlist(request):

    stu = Student.objects.all()

    serializer = StudentSerializer(stu,many=True)

    Json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(Json_data)

def teacherlist(request):

    tea = Teacher.objects.all()

    serializer = TeacherSerializer(tea,many=True)

    Json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(Json_data)