from django.urls import path
from .views import Tasklisk,TaskDetail


urlpatterns =[
    path('', Tasklisk.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task')
] 