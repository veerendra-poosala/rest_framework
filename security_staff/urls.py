
from django.urls import path,include

from security_staff import views
from rest_framework.routers import DefaultRouter

#creating urls for each functions in views
router=DefaultRouter()
router.register('mvs',views.secuirity_staffViewset,basename='floor_incharge')


urlpatterns = [
    path('',include(router.urls)),
    
]