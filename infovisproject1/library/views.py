from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
import requests
import json
import copy
# Create your views here.
from library.models import Subjects


def get_books_of_subjects(subject):
    response = requests.get('http://openlibrary.org/search.json?q=' + subject + '&limit=9')
    if response.status_code == 200:
        json_response = response.json()
        books = json_response['docs']
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
    # print(romance_books)
    return render(request, template, context)
    # return HttpResponse("Hello, world. You're at the polls index.")

def my_django_view(request):
    # for key in request.POST:
    #     print(key)
    # print(request.POST)
    # document = request.POST['document_item']
    # doc_json = json.loads(document)
    # subjects = doc_json['subject']
    # print(subjects)
    # a = ['romance','love']
    # results = Subjects.objects.filter(subject_text__iregex=r'(' + '|'.join(subjects) + ')').order_by('-hit_count')
    # context_data = []
    # for result in results:
    #     data = { 'name' : result.subject_text, 'hits': result.hit_count}
    #     context_data.append(data)
    #
    # print(type(result))
    # return JsonResponse(data, safe=False)
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
    keyword_with_plus = keywords.replace(" ","+")
    keywords_with_space = keywords
    current_page_number = int(request.GET['pagenum'])
    offset = (current_page_number - 1 )*10
    query = 'http://openlibrary.org/search.json?q='+ keyword_with_plus+'&&limit=10'
    if offset !=0:
        query = query + '&&offset=' + str(offset)
    response = requests.get(query)
    response2 = response.json()
    documents = response2['docs']
    # print(request.GET)

    # print(keywords_with_space)
    # romance_books = get_books_of_subjects("romance")
    # thriller_books = get_books_of_subjects("thriller");
    # arts_books = get_books_of_subjects("arts");
    context = {
        "searched_keywords": keywords_with_space,
        "searched_keywords_with_plus": keyword_with_plus,
        "documents"        : documents,
        "existing_page_num": current_page_number,
        "number_of_results": response2['numFound']
        # "romance_books" : romance_books,
        # "thriller_books": thriller_books,
        # "arts_books"    : arts_books
    }
    return render(request, template, context)
def document_details(request, olid):
    template = 'document_details_page_basic.html'
    # document_olid = olid
    # query = 'https://openlibrary.org/api/books?bibkeys=OLID:' + document_olid + '&jscmd=data&format=json'
    # r = requests.get(query)
    # response = r.json()
    # document = response['OLID:'+document_olid]
    context = {

    }
    return render(request, template, context)

def get_subject_match_data(request):
    document = request.POST['document_item']
    doc_json = json.loads(document)
    subjects = doc_json['subject']
    print(subjects)
    a = ['romance', 'love']
    results = Subjects.objects.filter(subject_text__iregex=r'(' + '|'.join(subjects) + ')').order_by('-hit_count')
    context_data = []
    for result in results:
        data = {'name': result.subject_text, 'hits': result.hit_count}
        context_data.append(data)

    # print(type(result))
    return JsonResponse(data, safe=False)