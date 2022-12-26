from django.urls import path

from . import views

urlpatterns = [
    path('Jyanti/', views.index, name='index'),
    path('sss', views.index, name='new_sss'),
    
]