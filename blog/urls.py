from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('getResponse', views.getResponse, name='getResponse'),
    path('speechtotext', views.speechtotext, name = 'speechtotext'),
    # path('speaktext', views.SpeakText, name = 'speaktext')
]