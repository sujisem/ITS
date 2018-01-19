from django.conf.urls import url,include
from django.views.generic import ListView, DetailView,TemplateView

from . import models
from webapps.models import Answers,Question,Replies,Session,Stdintxn,Student
from . import views
from .models import Question
from itertools import chain

"""all_models_dict = {
    "template_name": "webapps/home.html",
    "queryset": Question.objects.all(),
    "extra_context": {"question_list": Question.objects.all(),
                      "answers_list": Answers.objects.all(),
                      # and so on for all the desired models...
                      }
}"""

urlpatterns = [
    url(r'^$', views.getQuestion, name='index'),
    url(r'^processForm$',views.processForm,name='processForm')
    #url(r'^$', Question.as_view()),
    #url(r'^$', ListView.as_view(queryset=Question.objects.all(), template_name="webapps/home.html")),
     #url(r'^1$', ListView.as_view(queryset=Answers.objects.all(), template_name="webapps/answers.html")),
]