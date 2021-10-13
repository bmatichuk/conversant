from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Agent)
admin.site.register(Topic)
admin.site.register(Keyword)
admin.site.register(AgentTopic)
admin.site.register(topicKeyword)

admin.site.register(Movie_Info_genre)
admin.site.register(Movie_Info)