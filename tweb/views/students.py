from tweb import models
from django.shortcuts import render,redirect


def get_students(request):
    stu_list = models.Student.objects.all()
    for item in stu_list:
        return render(request,'get_students.html',{'stu_list':stu_list})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        for csl in  cs_list:
            return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method == 'POST':
        u = request.POST.get('name')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')

        models.Student.objects.create(
            name=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')

def del_students(request):
    nid= request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/students.html')

def edit_students(request):
    nid = request.GET.get('nid')
    obj = models.Student.objects.filter(id=nid).first()
    print(obj)
    cls_list = models.Classes.objects.values('id','title')
    print(cls_list)
    return render(request,'edit_classes.html',{'obj':obj,'cls_list':cls_list})