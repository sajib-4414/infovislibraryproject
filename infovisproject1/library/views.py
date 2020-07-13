from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
# Create your views here.



def index(request):
    # post = Post.objects.filter(status='published')
    template = 'index.html'
    context = {}
    return render(request, template, context)
    # return HttpResponse("Hello, world. You're at the polls index.")

def my_django_view(request):
    if request.method == 'GET':
        response = requests.get('http://openlibrary.org/subjects/romance.json?limit=5', params=request.GET)
    # else:
    #     r = requests.get('https://www.somedomain.com/some/url/save', params=request.GET)
    if response.status_code == 200:
        response2= response.json()
        key= response2['key']
        return HttpResponse(str(key))
    return HttpResponse('Could not save data'+str(response.status_code))