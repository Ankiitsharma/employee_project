from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('new/', views.add_new, name= 'new'),
    path('update_record/<str:pk>/', views.update_record, name= 'update'),
    path('delete_record/<str:pk>/', views.delete_record, name= 'delete'),
    path('login/', views.user_login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.logout_page, name= 'logout'),
]
