from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from speech_analyzer.judgeyou_nlp.yt_audio_extractor import get_audio
from speech_analyzer.judgeyou_nlp.speech_to_text import extract_text
from speech_analyzer.config import GRAMMARBOT_API_KEY

def analyze(request):
    # Get Video Link
    VIDEO_URL = request.POST['input-youtube-url']
    AUDIO_FILE = get_audio(VIDEO_URL)
    TEXT = extract_text(AUDIO_FILE)

    try:
        r = requests.post('http://bark.phon.ioc.ee/punctuator', data = {'text':TEXT})
        print(r.text)
    except:
        print('There\'s an error with the punctuator, try analyzing with google API instead')
        template = loader.get_template('speech/error.html')
        context = { 'error_msg': 'There\'s an error with the punctuator, try analyzing with google API instead' }
        return HttpResponse(template.render(context, request))

    PUNCTUATED_TEXT = r.text

    try:
        r = requests.get('http://api.grammarbot.io/v2/check?api_key=' + GRAMMARBOT_API_KEY + '&text=' + PUNCTUATED_TEXT + '&language=en')
        RESULT = r.json()
        print(RESULT)
    except:
        print('There\'s an error with grammarbot')
        template = loader.get_template('speech/error.html')
        context = { 'error_msg': 'There\'s an error with grammarbot, try analyzing with google API instead' }
        return HttpResponse(template.render(context, request))


    template = loader.get_template('speech/result.html')
    context = { 'result': RESULT }
    return HttpResponse(template.render(context, request))


def analyze_google(request):
    VIDEO_URL = request.POST['input-youtube-url']
