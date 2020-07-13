from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test-api-call/', views.my_django_view, name='my_django_view'),
]