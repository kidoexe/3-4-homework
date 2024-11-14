from django.shortcuts import render
from .models import get_random_students
import random

def main(request):
    students = get_random_students()
    student = random.choice(students)
    return render(request, 'students/templates/main.html', {'students': students})


def students(request):
    students = get_random_students()
    return render(request, 'students/templates/students.html', {'students': students})

