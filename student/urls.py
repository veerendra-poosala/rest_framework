
from django.urls import path
from .views import *

#creating urls for each functions in views


urlpatterns = [
    path('read',readStudentDetails),
    path('create',createStudentDetails),
    path('up/<int:id>',updateStudentDetails),
    path('del/<int:id>',deleteStudentDetails),
]