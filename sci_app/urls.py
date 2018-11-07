from django.contrib import admin
from django.urls import path
from sci_app import views

urlpatterns={
    path('', views.news, name='news'),  #нужно добавить редирект#
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about' ),
    path('requirements/', views.requirements, name='requirements' ),
    path('team/', views.team, name='team' ),
    path('conferences/', views.conferences, name='conferences' ),
    path('archive/',views.archive, name='archive'  ),

}