
from django.urls import path
from principal import views

#creating urls for each functions in views


urlpatterns = [
    path('clist/',views.listPrincipalDetails.as_view()),
    path('crud/<int:pk>/',views.RUDPrincipalDetails.as_view()),
    path('ccreate/',views.createPrincipalDetils.as_view()),

]