from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('speech/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

# TODO: index POST Request, receive youtube link