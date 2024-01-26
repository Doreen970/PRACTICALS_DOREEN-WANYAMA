from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

#these are functions that will handle our website capabilities

def add_student(request):
    """
    this is a function that takes in student data and creates a new student
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_students')
    else:
        form = StudentForm()

    return render(request, 'student_data/add_student.html', {'form': form})

def all_students(request):
    """
    a function that shows a list of all registered students
    """
    students = Student.objects.all()
    return render(request, 'student_data/all_students.html', {'students': students})


def view_student(request, student_id):
    """
    a view that shows information of each particular student
    """
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_data/student_detail.html', {'student': student})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('all_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_data/edit_student.html', {'form': form, 'student': student})
