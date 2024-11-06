from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('classes/', views.class_list, name='class_list'),
    path('add_student/', views.add_student, name='add_student'),
]