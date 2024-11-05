from django.shortcuts import render
from .models import Student, ClassSchedule

def student_list(request):
    students = Student.objects.all() # retrieves all student objects from database
    return render(request, 'enrollments/student_list.html', {'students': students})

def class_list(request):
    classes = ClassSchedule.objects.all() # retrieves all class schedule objects from database
    return render(request, 'enrollments/class_list.html', {'classes': classes})