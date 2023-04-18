from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse("data successfully submitted")
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO =Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']
        to=Topic.objects.get(topic_name=topic)
        
        wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
        wo.save()
        return HttpResponse("webpage is inserte successfully")
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LAO=Webpage.objects.all()
    d={'webpages':LAO}
    if request.method=='POST':
        name=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        wo=Webpage.objects.get(name=name)

        ao=Accessrecord.objects.get_or_create(name=wo,author=au,date=da)[0]
        ao.save()
        return HttpResponse("access is inserte successfully")
    return render(request,'insert_access.html',d)    



def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)
def radio(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'radio.html',d)