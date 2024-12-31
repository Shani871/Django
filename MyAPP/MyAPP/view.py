from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print("test the django Project ")



    if request.method =='POST':
        name = request.POST['name']
        print(name)
      
    isActive = True
    name = "Django"
    list = ["Home","About","Services","Contact"]
    student = {
        "Name":"Rahul",
        "Roll":101,
        "College":"IIT",
    }
    data={
        "isActive":isActive,
        "name":name,
        "list":list,
        "student":student,
    }
    return render(request, 'index.html',data)

def about(request):
    # return HttpResponse("About page")
    return render(request, 'about.html',{})

def services(request):
    # return HttpResponse(index.html)
    return render(request, 'services.html',{})

