from django.http.response import HttpResponse
from django.shortcuts import render
from .models import person
# Create your views here.
def index(request):
    return render(request,'index.html')


def form(request):
    if request.method == "POST" :
        username=request.POST["user_name"]
        name=request.POST["type"]
        age=request.POST["city"]
        sen=request.POST["age"]
        friendtype = ""
        if name == "infp":
            friendtype = "entj"
        if name == "enfp":
            friendtype = "intj"
        if name == "infj":
            friendtype = "entp"
        if name == "enfj":
            friendtype = "infp"
        if name == "intj":
            friendtype = "enfp"
        if name == "entj":
            friendtype = "intp"
        if name == "intp":
            friendtype = "estj"
        if name == "entp":
            friendtype = "infj"
        if name == "isfp":
            friendtype = "esfj"
        if name == "esfp":
            friendtype = "istj"
        if name == "istp":
            friendtype = "esfj"
        if name == "estp":
            friendtype = "isfj"
        if name == "isfj":
            friendtype = "esfp"
        if name == "esfj":
            friendtype = "istp"
        if name == "istj":
            friendtype = "esfp"
        if name == "estj":
            friendtype = "isfp"
        person.objects.create(username=username, type=name,city=age,type_cmplement=friendtype,sen=sen)
        u=person.objects.filter(type=friendtype)
        output={"result":u}
        return render(request,'result.html',context =output)
    elif request.method == "GET" :
        return render(request,"form.html")


