# these show the urls path for my website

from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('students/', views.all_students, name='all_students'),
    path('students/<int:student_id>/', views.view_student, name='view_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'), 
]