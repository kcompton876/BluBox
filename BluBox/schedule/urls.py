from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.show_home),
    # path('home/', views.show_home),
    path('instructor_list/', views.show_instructor_list),
    path('register/', views.show_register),
    path('login/', views.show_login),
]