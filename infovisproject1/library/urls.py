from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_result, name='search_result'),
    path('test-api-call/', views.my_django_view, name='my_django_view'),
]