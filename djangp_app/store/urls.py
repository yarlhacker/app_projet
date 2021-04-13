from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('viewsphoto/<str:pk>', views.views ,name='view'),
]