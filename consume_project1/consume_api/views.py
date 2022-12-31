from django.shortcuts import render
import requests
from .models import Student


# Create your views here.
def home(request):

    response = requests.get('http://localhost:8000/stuinfo/').json()
    print(">>>>>>",response)
    for i in response:
        id = i['id']
        name = i['name']
        rollno = i['rollno']
        city = i['city']
    
    if Student.objects.filter(pk=id).exists():
        pass
    else:
        stu = Student.objects.create(id =id ,name = name , rollno =rollno , city = city)
        print(stu)
        stu.save()


    context = {'response' : response}

    return render(request,'home.html', context)
