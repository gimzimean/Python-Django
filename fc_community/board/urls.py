from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.board_list),  # 경로, 함수
    path('write/', views.board_write),  # 경로, 함수
    path('detail/<int:pk>/', views.board_detail),  # 경로, 함수
]
