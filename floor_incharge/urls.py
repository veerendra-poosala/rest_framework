
from django.urls import path,include

from floor_incharge import views
from rest_framework.routers import DefaultRouter

#creating urls for each functions in views
router=DefaultRouter()
router.register('vs',views.floor_incharegeViewset,basename='floor_incharge')


urlpatterns = [
    path('',include(router.urls)),
    
]