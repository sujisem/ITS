from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
"""
from .models import Question
from .models import Answers
from .models import Replies

def customView(request):
	all_qns=Replies.objects.all()
	html=''
	for qn in all_qns:
		html+=qn.desc
	return HttpResponse("<b>"+html+"</b>")"""

def index(request):
    ##all_qns=Replies.objects.all()
    template = loader.get_template('its/customView.html')
    ##print(Replies.objects.count())
    context = {
        'all_qns': [],
    }
    return HttpResponse(template.render(context, request))