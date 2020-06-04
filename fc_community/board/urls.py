from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.board_list),  # 경로, 함수
]
