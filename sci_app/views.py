from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def news(request):
    page_name = "новости"
    return render(request, '../templates/news.html',)

def about(request):
    page_name = "о журнале"
    return render(request,'../templates/about.html',)

def requirements(request):
    page_name = "материалы"
    return render(request,'../templates/requirements.html',)

def team(request):
    page_name = "коллегия"
    sub_neader = "Редакционная коллегия"
    return render(request,'../templates/team.html',)

def conferences(request):
    page_name = "конференции"
    return render(request,'../templates/conferences.html' ,)

def archive(request):
    page_name = "Архив"
    sub_neader = "Архив журнала"
    return render(request,'../templates/archive.html' ,)

