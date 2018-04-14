from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext

# Create your views here.


def index(request):
    template = loader.get_template('fokus/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))