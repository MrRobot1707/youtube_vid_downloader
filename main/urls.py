from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('download/',views.download,name="download"),
    path('download/startdownloding/',views.startdownloding,name="startdownloding"),
    
]

