from django.forms import ModelForm
from .models import *

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name',)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age',)
