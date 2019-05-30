from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from speech_analyzer.judgeyou_nlp.yt_audio_extractor import get_audio
from speech_analyzer.judgeyou_nlp.speech_to_text import extract_text

def analyze(request):
    # Get Video Link
    VIDEO_URL = request.POST['input-youtube-url']
    AUDIO_FILE = get_audio(VIDEO_URL)
    TEXT = extract_text(AUDIO_FILE)
    
    template = loader.get_template('speech/result.html')
    context = {}
    return HttpResponse(template.render(context, request))