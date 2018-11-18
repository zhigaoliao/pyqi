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

def set_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        cot = models.Classes.objects.filter(id=nid).first()
        tall = cot.m.all().values_list('id','name')
        idlist = list(zip(*tall))[0] if list(zip(*tall)) else []

        allteacher =models.Teachers.objects.all()
        return render(request,
                        'set_teacher.html',
                        {
                        'idlist':idlist,
                        'allteacher':allteacher,
                        'nid':nid
                        }
                        )
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        ids = request.POST.getlist('tids')
        print('当前班级的ID', nid ,'分配老师的ID', ids)

        obj = models.Classes.objects.filter(id=nid).first()
        obj.m.set(ids)
        return redirect('/classes.html')