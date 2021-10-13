from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from handlerapp.forms import *
from handlerapp.models import *
import os

from .models import *


@login_required
def dashboard(request):
    Login_Agent = request.user.username
    if request.user.is_authenticated:
        print("Logged in")
    return render(request, 'dashboard.html',{'Login_Agent':Login_Agent})

@login_required
def IndexExtend(request):
    Login_Agent = request.user.username
    if request.user.is_authenticated:
        print("Logged in")

    return render(request, 'DashboardExtend.html',{'Login_Agent':Login_Agent})


@login_required
def Agent_view(request):
    if request.method == 'POST':
        Login_Agent = User.objects.get(username=request.user.username)
        Name = request.POST['name_agent']
        Visibility = request.POST['text']
        Description = request.POST['comments']
        print(Login_Agent,Name,Visibility,Description)
        obj = Agent.objects.create(
            Creator = Login_Agent ,
            name = Name,
            visibility = Visibility,
            description = Description)
    return render(request,'create_agent.html')


@login_required
def Keywords(request):
    if request.method == 'POST':
        word = request.POST['key_s']
        definition = request.POST['w3review']
        obj = Keyword(word=word,definition=definition)
        obj.save()
    return render(request,'keyword.html')





@login_required
def Topics(request):
    Login_Agent = User.objects.get(username=request.user.username)
    print(Login_Agent.id)
    s = Login_Agent.id
    Agent_list = Agent.objects.all()
    show_agents = []
    for i in Agent_list:
        print(i.name)
        show_agents.append(i.name)
    if request.method == 'POST':
        topic_names = request.POST['topic_name']
        topic_descriptions = request.POST['w3review']
        TopicInfo = Topic.objects.create(name=topic_names,description=topic_descriptions)
        
    return render(request,'topic.html',{'name':show_agents})

@login_required
def List_Agent_view(request):
    Login_Agent = User.objects.get(username=request.user.username)
    lists = Agent.objects.filter(Creator=Login_Agent)
    print("lists:--",lists)
    name_agent = []
    name_id = []
    name_description = []
    for agent in lists:
        print(agent.Agent_id)
        name_id.append(agent.Agent_id)
        name_agent.append(agent.name)
        name_description.append(agent.description)
    print(name_agent)
    show_agent = zip(name_agent,name_id,name_description)
    return render(request,'list_agent.html',{'list':show_agent})




@login_required
def Topics_Agent(request):

    user_id =  request.GET.get('info')
    user_ids = Agent.objects.get(name=user_id)
    topis_all = AgentTopic.objects.filter(agent=user_ids)
    topic_of_agent = []
    dis = []
    for x in topis_all:
        # for person in x.agent.all():
        #     print(person.name)
        for person in x.topic.all():
            topic_of_agent.append(person.name)
        for person in x.topic.all():
            # topic_of_agent.append(person.description)
            dis.append(person.description)
    print(topic_of_agent)
    topic_of = zip(topic_of_agent,dis)
    return render(request,'agentwithtopic.html',{'topica':topic_of,'user_id':user_id})



def keyword_topic_show(request):
     key_info = request.GET.get('info')
     topicID = Topic.objects.get(name=key_info)
     topis_all = topicKeyword.objects.filter(topics=topicID)
     keyword_list = []
     key_definition = []
     for x in topis_all:
        for person in x.topics.all():
            print(person.name)
        for person in x.keywords.all():
            keyword_list.append(person.word)
        for person in x.keywords.all():
            key_definition.append(person.definition)

     show = zip(keyword_list,key_definition)
     return render(request, 'keywordwithtopic.html', {'keyword_list': show,'key_info':key_info})



@login_required
def Agent_with_topic(request):
    lists = Agent.objects.all()
    print('/*/*/')
    name_agent = []
    for agent in lists:
        print(agent.Agent_id)
        name_agent.append(agent.name)

    lists = Topic.objects.all()
    name_agent_topic = []
    for agent in lists:
        name_agent_topic.append(agent.name)
    if request.method == 'POST':
        Agent_selects = request.POST['select']
        Agent_sele = request.POST['test']
        Agent_name = Agent.objects.get(name=Agent_selects)
        Agent_Topic = Topic.objects.get(name=Agent_sele)
        print(Agent_Topic.Topic_id)
        print(Agent_name.Agent_id,)
        AgentGenre = AgentTopic.objects.create()
        AgentGenre.agent.add(Agent_name.Agent_id)
        AgentGenre.topic.add(Agent_Topic.Topic_id)
    print(name_agent,name_agent_topic)
    return render(request,'combine_agent_topic.html',{'name_agent':name_agent,'name_agent_topic':name_agent_topic})


def chat_bot(request):
    return render(request, 'chatbot.html')
@login_required
def Topic_with_keyword(request):
    lists = Keyword.objects.all()
    name_keyword = []
    for keyword in lists:
        name_keyword.append(keyword.word)
    Topic_lists = Topic.objects.all()
    name_agent_topic = []
    for Topics in Topic_lists:
        name_agent_topic.append(Topics.name)
    print(name_agent_topic)
    if request.method == 'POST':
        key_selects = request.POST['select']
        Agent_sele = request.POST['test']
        Agent_name = Keyword.objects.get(word=key_selects)
        Agent_Topic = Topic.objects.get(name=Agent_sele)
        print(Agent_Topic.Topic_id)
        print(Agent_name.Keyword_ids,)
        AgentGenre = topicKeyword.objects.create()
        AgentGenre.topics.add(Agent_Topic.Topic_id)
        AgentGenre.keywords.add(Agent_name.Keyword_ids)
    return render(request,'combine_topic_keyword.html',{'name_keyword':name_keyword,'Topic_list':name_agent_topic})










def signup_page(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            name=request.POST["Name"]
            email=request.POST["Email"]
            password=request.POST["Password"]
            Firstname=request.POST["Firstname"]
            lastname=request.POST["lastname"]
            user = User.objects.create_user(username=name,email=email,password=password,first_name=Firstname,last_name=lastname)
            user.save()
            return redirect('/')
    else:
        form = signupform()
        print("notdshksfdhjsdfhsdfahlsafd")
    return render(request,'signup.html',{"form":form})

def login_user(request):
    if request.user.is_authenticated:
        print("Logged in")
        return redirect("/dashboard/")
    else:
        print("Not logged in")

    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = request.POST.get('Username')
            print(username)
            password = request.POST.get('Password')
            print(password)
            user = authenticate(username=username, password=password)
            if user:
                print("yesssssssssssssssss")
                login(request,user)
                return redirect("/dashboard/")

    else:
        form = loginform()
        print("not")
    return render(request, 'signin.html', {"form": form})



@login_required
def user_logout(request):
    logout(request)
    return redirect('/')



