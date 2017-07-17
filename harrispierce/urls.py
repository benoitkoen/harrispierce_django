from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.DisplayView, name='display'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.IndexPersoView, name='index_perso'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.DisplayPersoView, name='display_perso'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.DisplaySearchView, name='display_search'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.LoginView, name='login'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.NewUserView, name='new_user')
]
