from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework.views import APIView


# Create your views here.
class Student_Api(APIView):

    def get(self,request,pk=None,format = None):

        id=pk
        if id is not None:

            stu = Student.objects.get(pk=id)

            serializer = StudentSerializer(stu)

            return Response(serializer.data)

        else:

            stu = Student.objects.all()

            serializer = StudentSerializer(stu, many = True)

            return Response(serializer.data)

    def post(self,request,format=None):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            dic = {'msg': 'Data created'}
            return Response(dic)
        else:
            dic = {'msg':'Invalid input'}
            return Response(dic)
            
    def put(self,request,pk=None,format=None):

        id=pk

        stu = Student.objects.get(pk=id)

        serializer = StudentSerializer(stu,data= request.data,partial = True)

        if serializer.is_valid():
            serializer.save()
            dic = {'msg':'Data Updated'}
            return Response(dic)
        else:
            dic = {'msg':'Data not updated'}
            return Response(dic)

    def delete(self,request,pk=None,format=None):

        id=pk

        stu = Student.objects.get(pk=id)

        stu.delete()

        dic = {'msg':'Data Deleted'}

        return Response(dic)