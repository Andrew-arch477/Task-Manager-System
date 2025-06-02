from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Task_ViewPage.as_view(), name='Task_main_page'),
    path('task_create/', views.Task_Create.as_view(), name='Task_create_page'),
    path('task_update/<str:pk>', views.Task_Update.as_view(), name='Task_update_page'),
    path('task_delete/<str:pk>', views.Task_Delete.as_view(), name='Task_delete_page'),

    path('login/', views.Login_View.as_view(), name='login_page'),
    path('logout/', views.Logout_View.as_view(), name='logout_page'),
    path('registration/', views.Registration_View.as_view(), name='registration_page'),

    path('comment/<str:pk>', views.Comment_Create_View.as_view(), name='comment_page'),
    path('comment_update/<str:pk>', views.Comment_Update_View.as_view(), name='comment_update_page'),
    path('comment_delete/<str:pk>', views.Comment_Delete_View.as_view(), name='comment_delete_page'),
]