from qa.views import test
from django.conf.urls import url

urlpatterns = [
    url(r'^', test),
]
