from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<record_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<record_id>[0-9]+)/results/$', views.steps, name='steps'),
    # ex: /polls/5/vote/
    url(r'^(?P<record_id>[0-9]+)/vote/$', views.createStep, name='createStep'),
]