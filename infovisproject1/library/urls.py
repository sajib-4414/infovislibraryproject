from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_result, name='search_result'),
    path('document-details/<str:olid>/', views.document_details, name='details'),
    path('test-api-call/', views.my_django_view, name='my_django_view'),
    path('get-subject-matches/', views.get_subject_match_data, name='get_subject_match_data'),
]