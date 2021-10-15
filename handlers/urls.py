"""handlers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from handlerapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup_page, name='signup'),
    path('',views.login_user, name='signin'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.user_logout, name='user_logout'),

    path('agent/',views.Agent_view, name='Agent View'),
    path('Index/',views.IndexExtend, name='Index Extend View'),
    path('List/',views.List_Agent_view, name='Agent View'),
    path('keyword/',views.Keywords,name='Keyword'),
    path('Topic/',views.Topics, name='Topic'),
    path('A/',views.Topics_Agent, name='A'),
    path('AgentWithTopic/',views.Agent_with_topic, name='A'),
    path('TopicWithKeyword/',views.Topic_with_keyword, name='A'),
    path('Chat/',views.chats, name='chat'),
    path('Key/',views.keyword_topic_show, name='Key'),
    path('chatting/',views.chatting, name='chatting'),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
