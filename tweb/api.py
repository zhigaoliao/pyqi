from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.views.decorators import csrf

def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request,"student.html", ctx)
