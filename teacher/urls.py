
from django.urls import path
from teacher import views

#creating urls for each functions in views


urlpatterns = [
    path('mread',views.readTeacherDetails.as_view()),
    path('mup/<int:pk>/',views.updateTeacherDetails.as_view()),

]