from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),  # 경로, 함수
    path('login/', views.login),  # 경로, 함수
    path('logout/', views.logout),  # 경로, 함수
]
