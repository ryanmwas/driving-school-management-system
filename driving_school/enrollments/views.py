from django.shortcuts import render
from .models import Student, ClassSchedule
from django.contrib.auth.decorators import login_required
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all() # retrieves all student objects from database
    return render(request, 'enrollments/student_list.html', {'students': students})

def class_list(request):
    classes = ClassSchedule.objects.all() # retrieves all class schedule objects from database
    return render(request, 'enrollments/class_list.html', {'classes': classes})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'enrollments/add_student.html', {'form': form})