from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
# Create your views here.


def get_books_of_subjects(subject):
    response = requests.get('http://openlibrary.org/subjects/' + subject + '.json?limit=9')
    if response.status_code == 200:
        json_response = response.json()
        books = json_response['works']
        return books
    return []


def index(request):
    # post = Post.objects.filter(status='published')
    template = 'index.html'
    romance_books = get_books_of_subjects("romance")
    thriller_books = get_books_of_subjects("thriller");
    arts_books = get_books_of_subjects("arts");
    context = {
        "romance_books" : romance_books,
        "thriller_books": thriller_books,
        "arts_books"    : arts_books
    }
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

def search_result(request):
    # post = Post.objects.filter(status='published')
    template = 'search-results-page-basic.html'
    keywords = request.GET['keywords']
    keywords_with_space = keywords.replace("+"," ")
    query = 'http://openlibrary.org/search.json?q='+ keywords+'&&limit=10'
    response = requests.get(query)
    response2 = response.json()
    documents = response2['docs']

    # print(keywords_with_space)
    # romance_books = get_books_of_subjects("romance")
    # thriller_books = get_books_of_subjects("thriller");
    # arts_books = get_books_of_subjects("arts");
    context = {
        "searched_keywords": keywords_with_space,
        "documents"        : documents
        # "romance_books" : romance_books,
        # "thriller_books": thriller_books,
        # "arts_books"    : arts_books
    }
    return render(request, template, context)