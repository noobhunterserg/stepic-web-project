"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from qa.views import notfound, test, new, popular, question, add_question, add_answer, add_like

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<num>[0-9]+)/$', question, name='question_page'),
    url(r'^question/(?P<num>[0-9]+)/addanswer/$', add_answer, name='add_answer'),
    url(r'^question/(?P<num>[0-9]+)/addlike/$', add_like, name='add_like'),
    url(r'^ask/', add_question, name='new_question'),
    url(r'^popular/', popular, name='popular'),
    url(r'^', notfound),
]

# urlpatterns += staticfiles_urpatterns()
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
