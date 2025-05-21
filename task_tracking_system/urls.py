from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Task_main/', views.Task_ViewPage.as_view(), name='Task_main_page'),
    path('Task_create/', views.Task_Create.as_view(), name='Task_create_page'),
]