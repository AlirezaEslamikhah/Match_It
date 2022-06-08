from django.http.response import HttpResponse
from django.shortcuts import render
from .models import person
# Create your views here.
def index(request):
    return render(request,'index.html')


def form(request):
    if request.method == "POST" :
        username=request.POST["user_name"]
        name=request.POST["lastname"]
        age=request.POST["age"]
        email=request.POST["my_email"]
        password=request.POST["user_pass"]
        person.objects.create(username=username, name=name,age=age,email=email,password=password)
        name_dorost = "Alireza"
        user_dorost = "Alireza_1080"
        age_dorost = "19"
        email_dorost = "alirezasl2014@gmail.com"
        pass_dorost="1080"
        user = person(username=user_dorost,name=name_dorost,age=age_dorost,email=email_dorost,password=pass_dorost)
        output={"result" : user}
        return render(request,'result.html',context=output)
    elif request.method == "GET" :
        return render(request,"form.html")

