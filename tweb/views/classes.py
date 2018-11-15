from tweb import models
from django.shortcuts import render,redirect

def get_classes(request):
    cls_list = models.Classes.objects.all()
    for item in cls_list:
        return render(request,'get_classes.html',{'cls_list':cls_list})

def add_classes(request):
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method =="POST":
        title = request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect('/classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,'edit_classes.html',{'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('xxoo')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')