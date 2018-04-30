from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render

from app.backend import fi

def index(request):
    return render(request, 'index.html')


def get(request):
    print(request.POST.get('text'))

    keywords_yes = [keyword.strip() for keyword in filter(None, request.POST.get('text').split(','))]
    keywords_no = []

    articles = fi.find(keywords_yes, keywords_no)

    return JsonResponse({ 'articles': articles })


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
