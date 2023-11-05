from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='list'),
    path('student/', StudentView.as_view(), name='student'),
    path('teacher/', TeacherView.as_view(), name='teacher')
]
