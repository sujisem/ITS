from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Answers, Stdintxn, Student, Session, Replies
import datetime
import random
from django.views.generic import ListView, DetailView, TemplateView

excludeList = []
random.seed(1)


# Create your views here.
def index1(request):
    """ data = Question.objects.all()
     return render(request, 'webapps/home.html',
                   context={'data':data},)"""
    return render(request, 'webapps/home.html')


"""class Question(DetailView):
    model = Question
    template_name = 'webapps/home.html'

    def get_context_data(self, **kwargs):
        context = super(Question, self).get_context_data(**Kwargs)
        context['answers'] = Answers.objects.all()
        return context"""


def customView(request):
    all_qns = Question.objects.all()
    html = ''
    for qn in all_qns:
        html += qn.desc
    return HttpResponse("<b>" + html + "</b>")


def index(request):
    if request.method == 'POST':
        alldata = request.POST
    else:
        alldata = request.GET
    # change the request parameter name. I have given it as a 'data'
    print(alldata.get("data", "0"))
    all_qns = Question.objects.all()
    all_ans = Answers.objects.all()
    print(len(all_ans))
    template = loader.get_template('webapps/view.html')
    context = {
        'all_qns': all_qns,
        'all_ans': all_ans,
    }
    return HttpResponse(template.render(context, request))


def getQuestion(request):
    print("get Question")
    session_id = request.session._session_key
    if not session_id:
        request.session.save()
    session_id = request.session.session_key
    t = Session(id=session_id, start=datetime.datetime.now(), end=datetime.datetime.now())
    t.save()
    template = loader.get_template('webapps/view.html')
    ## random number generation by excluding from the list.
    # exclude list - global variable.
    # qlist=Question.objects.all().values_list('id')
    qlist = []
    if 'list10' in request.session:
        qlist = request.session['list10']
        for q in qlist:
            print(q)
        print("chosing from session")
        qnChosen = random.choice(qlist)
    else:
        qnChosen = 1
        print("chosing in else")
        request.session['list10'] = [2, 3]

    """
    if 'exclude_list' in request.session:
        print("inside exclude list")
        qlist = set(qlist)
        excludeList= request.session['exclude_list']
        for i in excludeList:
            print(i)
        excludeList=set(excludeList)
        qlist=qlist-excludeList
        qlist = list(qlist)
    else:
        request.session['exclude_list']=[]
    """
    # qnChosen=random.choice(qlist)
    # qlist.remove(qnChosen)
    print(qnChosen)
    qn = Question.objects.filter(id=qnChosen)  # add the condition
    opt = Answers.objects.filter(qnid=qnChosen)  # add the condition
    context = {
        'qn': qn,
        'opt': opt
    }
    return HttpResponse(template.render(context, request))


def processForm(request):
    print("Process form")
    if request.method == 'POST':
        formData = request.POST
    else:
        formData = request.GET
    qnid = formData.get("qnid")
    uansid = formData.get("options")
    print(qnid)
    print(uansid)
    ans = Answers.objects.filter(qnid=qnid, id=uansid)
    if ans[0].iscorrect:
        return stdIntxnUpdate(request, qnid, uansid)
        # print("correct")
    else:
        return userReply(request, qnid, uansid)
        # print("its not correct")


def stdIntxnUpdate(request, qnid, ans):
    intxn = Stdintxn(sessid=Session.objects.get(id=request.session._session_key), qnid=Question.objects.get(id=qnid),
                     ansid=Answers.objects.get(qnid=qnid, id=ans), stdid=Student.objects.get(id=1), attempt=1)
    intxn.save()
    ex_set = request.session['exclude_list']
    ex_set += [qnid]
    request.session['exclude_list'] = ex_set
    return getQuestion(request)


def userReply(request, qnid, uansid):
    print("userReply")
    print(qnid)
    print(uansid)
    reply = Replies.objects.filter(qnid=qnid)  # ,ansid=uansid)
    # get the reply from the database.
    print(len(reply))
    repid = random.randint(0, len(reply) - 1)
    print(repid)
    msg = reply[repid].desc
    print(msg)
    return repeatQuestion(request, qnid, msg)


def repeatQuestion(request, qnid, msg):
    print("Repeat Question")
    template = loader.get_template('webapps/view.html')
    qn = Question.objects.filter(id=qnid)
    opt = Answers.objects.filter(qnid=qnid)
    context = {
        'qn': qn,
        'opt': opt,
        'msg': msg
    }
    return HttpResponse(template.render(context, request))


def generateReply(request, qnid):
    reps = Replies.objects.filter(qnid=qnid)
    dict = {}
    dict[qnid] = {}
    for rep in reps:
        dict[qnid][rep.ansid] = []
    for rep in reps:
        dict[qnid][rep.ansid] += [rep.id]






