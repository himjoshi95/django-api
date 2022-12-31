from functools import partial
from django.http import HttpResponse 
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_list(request):

    if request.method == 'GET':
        

        stu = Student.objects.all()

        serializer = StudentSerializer(stu , many =True)

        Json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(Json_data, content_type = 'application/json')

    if request.method == 'POST':

        json_data = request.body

        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        print(python_data)

        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            serializer.save()
        
        dic = { 'Msg':'Data posted successfully'}

        json_data = JSONRenderer().render(dic)

        return HttpResponse(json_data , content_type = 'application/json')

    if request.method == 'PUT':

        json_data = request.body

        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stu = Student.objects.get(id=id)

        serializer = StudentSerializer(stu, data= python_data , partial =True)

        if serializer.is_valid():
            serializer.save()

        dic = { 'Msg':'Data Updated successfully'}

        json_data = JSONRenderer().render(dic)

        return HttpResponse(json_data , content_type = 'application/json')

    if request.method == 'DELETE':

        json_data = request.body

        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stu = Student.objects.get(id=id)

        stu.delete()

        dic = { 'Msg':'Data Deleted successfully'}

        json_data = JSONRenderer().render(dic)

        return HttpResponse(json_data , content_type = 'application/json')



        

        







    
