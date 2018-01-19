from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question,Answers,Stdintxn,Student,Session,Replies
import datetime
import random
from django.views.generic import ListView, DetailView,TemplateView

answered_qn='answered_qn'
random.seed(10)

def index(request):
    if request.method == 'POST' :
        alldata=request.POST
    else:
        alldata = request.GET
    print(alldata.get("data","0"))
    all_qns=Question.objects.all()
    all_ans = Answers.objects.all()
    print(len(all_ans))
    template = loader.get_template('webapps/view.html')
    context = {
        'all_qns' : all_qns,
        'all_ans' : all_ans,
    }
    return HttpResponse(template.render(context,request))

def getQuestion(request):
    print("get Question")
    session_id= request.session._session_key
    if not session_id:
        request.session.save()
    session_id = request.session.session_key
    t=Session(id=session_id,start=datetime.datetime.now(),end=datetime.datetime.now())
    t.save()
    template = loader.get_template('webapps/view.html')
    qlist1=list(Question.objects.all().values_list('id'))
    qlist=[]
    for i in qlist1:
        for j in i:
            qlist.append(j)
    excludeList=[]
    if answered_qn in request.session:
        excludeList = list(request.session[answered_qn])
        print(excludeList)
        for i in excludeList:
            qlist.remove(int(i))
    else:
        request.session[answered_qn]=[]
    qnChosen=random.choice(qlist)
    qn=Question.objects.filter(id=qnChosen) # add the condition
    opt=Answers.objects.filter(qnid=qnChosen) # add the condition
    excludeList.append(qnChosen)
    context = {
        'qn': qn,
        'opt': opt
    }
    return HttpResponse(template.render(context,request))

def processForm(request):
    if request.method == 'POST':
        formData=request.POST
    else:
        formData = request.GET
    qnid=formData.get("qnid")
    uansid=formData.get("options")
    ans=Answers.objects.filter(qnid=qnid,id=uansid)
    if ans[0].iscorrect:
        return stdIntxnUpdate(request,qnid,uansid)
    else :
        return userReply(request,qnid,uansid)

def stdIntxnUpdate(request,qnid,ans):
    intxn=Stdintxn(sessid=Session.objects.get(id=request.session._session_key),qnid=Question.objects.get(id=qnid),
                   ansid=Answers.objects.get(qnid=qnid,id=ans),stdid=Student.objects.get(id=1),attempt=1)
    intxn.save()
    excludeList=request.session[answered_qn]
    excludeList.append(qnid)
    request.session[answered_qn] = excludeList
    return getQuestion(request)


def userReply(request,qnid,uansid):
    print("userReply")
    print(qnid)
    print(uansid)
    reply=Replies.objects.filter(qnid=qnid)
    print(len(reply))
    repid=random.randint(0,len(reply)-1)
    print(repid)
    msg=reply[repid].desc
    print(msg)
    return repeatQuestion(request,qnid,msg)

def repeatQuestion(request,qnid,msg):
    print("Repeat Question")
    template = loader.get_template('webapps/view.html')
    qn = Question.objects.filter(id=qnid)
    opt = Answers.objects.filter(qnid=qnid)
    context = {
        'qn': qn,
        'opt': opt,
        'msg':msg
    }
    return HttpResponse(template.render(context, request))

def generateReply(request,qnid):
   reps=Replies.objects.filter(qnid=qnid)
   dict={}
   dict[qnid]={}
   for rep in reps:
       dict[qnid][rep.ansid]=[]
   for rep in reps:
       dict[qnid][rep.ansid]+=[rep.id]




    

