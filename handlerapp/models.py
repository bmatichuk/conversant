from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Movie_Info_genre(models.Model):
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.genre
class Movie_Info(models.Model):
    id             = models.AutoField(primary_key=True)
    title          = models.CharField(max_length=100, blank=True, null=True)
    overview       = models.TextField(blank=True, null=True)
    release_date   = models.CharField(max_length=10, blank=True, null=True)
    genres         = models.ManyToManyField(Movie_Info_genre)
    def __str__(self):
        return self.title




class Agent(models.Model):
    Agent_id        =   models.AutoField(primary_key=True)
    Creator         =   models.ForeignKey(User, on_delete=models.CASCADE)
    name            =   models.CharField(max_length=100,editable=True, blank=True)
    description     =   models.CharField(max_length=100,editable=True, blank=True)
    visibility      =   models.CharField(max_length=100,editable=True, blank=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    Topic_id=models.AutoField(primary_key=True, blank=True)
    name =  models.CharField(max_length=100,editable=True, blank=True)
    description = models.CharField(max_length=100,editable=True, blank=True)
    def __str__(self):
        return self.name

class AgentTopic(models.Model):
    name_id = models.AutoField(primary_key=True, blank=True)
    agent = models.ManyToManyField(Agent)
    topic = models.ManyToManyField(Topic)
    # def __str__(self):
    #     return self.topic
        # return "Agent "+str(self.agent)+ "  ==Topic "+str(self.topic)

class Keyword(models.Model):
    Keyword_ids = models.AutoField(primary_key=True, blank=True)
    word = models.CharField(max_length=100,editable=True, blank=True)
    definition = models.CharField(max_length=100,editable=True, blank=True)
    def __str__(self):
        return self.word

class topicKeyword(models.Model):
    Keyword_Id = models.AutoField(primary_key=True, blank=True)
    topics = models.ManyToManyField(Topic)
    keywords = models.ManyToManyField(Keyword)
    def __str__(self):
        return "Topic "+str(self.topics)+"==Keyword "+str(self.keywords)


class variable(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  
    name=models.CharField(max_length=100,editable=True, blank=True)
    description=models.CharField(max_length=100,editable=True, blank=True)

    def __str__(self):
        return "Topic "+str(self.Topic)+"==variable "+str(self.name)

class operations(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  
    name=models.CharField(max_length=100,editable=True, blank=True)
    description=models.CharField(max_length=100,editable=True, blank=True)
    pre_condition=models.CharField(max_length=255,editable=True, blank=True)
    effect=models.CharField(max_length=255,editable=True, blank=True)
    def __str__(self):
        return "Topic "+str(self.Topic)+"==operations "+str(self.name)

class conversation(models.Model):
    conversation_id=models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)  
    startdate=models.CharField(max_length=100,editable=True, blank=True)

    def __str__(self):
        return "Topic "+str(self.Topic)+"==operations "+str(self.name)


# class entry(models.Model):
#     participants=models.CharField(max_length=100,editable=True)
#     conversation = models.ForeignKey(conversation, on_delete=models.CASCADE)
#     def __str__(self):
#         return "Topic "+str(self.Topic)+"==operations "+str(self.name)




