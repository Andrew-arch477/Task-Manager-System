from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('task_main/', views.Task_ViewPage.as_view(), name='Task_main_page'),
    path('task_create/', views.Task_Create.as_view(), name='Task_create_page'),
    path('task_update/<str:pk>', views.Task_Update.as_view(), name='Task_update_page'),
    path('task_delete/<str:pk>', views.Task_Delete.as_view(), name='Task_delete_page'),
    path('login/', views.Login_View.as_view(), name='login_page'),
]