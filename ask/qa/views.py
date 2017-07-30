from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfound(request, *args, **kwargs):
    return HttpResponseNotFound('Not Found!')

def main(request):
    return render(request, 'index.html')

def questions(request):
    return render(request, 'main_page.html')
