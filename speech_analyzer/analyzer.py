from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def analyze(request):
    video_link = request.POST['input-youtube-url']
    print(video_link)
    template = loader.get_template('speech/result.html')
    context = {}
    return HttpResponse(template.render(context, request))