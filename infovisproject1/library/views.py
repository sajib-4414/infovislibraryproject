from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    # post = Post.objects.filter(status='published')
    template = 'index.html'
    context = {}
    return render(request, template, context)
    # return HttpResponse("Hello, world. You're at the polls index.")
