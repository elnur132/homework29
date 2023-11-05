from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import TeacherForm, StudentForm
from .models import Teacher, Student

# Create your views here.
class TeacherView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'create_teacher.html'
    success_url = reverse_lazy('list')

class StudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'create_student.html'
    success_url = reverse_lazy('list')
    
class DashboardView(ListView):
    model = Student
    template_name = 'list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.values('age')