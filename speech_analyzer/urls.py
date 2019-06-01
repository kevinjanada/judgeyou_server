from django.urls import path
from . import analyzer
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', analyzer.analyze, name='analyze'),
    path('analyze-google', analyzer.analyze_google, name='analyze-google')
]