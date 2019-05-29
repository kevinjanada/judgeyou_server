from django.urls import path
from speech_analyzer import analyzer
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', analyzer.analyze, name='analyze')
]