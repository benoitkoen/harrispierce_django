from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView
from . import views

from harrispierce.models import Article

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^display.html/$', views.DisplayView.as_view(), name='display'),
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',
    #    views.DisplayView.as_view(),
    #    name="display"),

    # ex: /polls/5/results/
    url(r'^login/index_perso.html/$', views.IndexPersoView.as_view(), name='index_perso'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.DisplayPersoView, name='display_perso'),
    # ex: /polls/5/vote/
    url(r'^login/search_form.html/$', views.SearchFormView.as_view(), name='search_form'),
    url(r'^login/display_search.html/$', views.DisplaySearchView.as_view(), name='display_search'),
    url(r'^harrispierce/must_be_loggedin.html/$', views.MustBeLoggedInView.as_view(), name='must_be_loggedin'),


    #url(r'^login/display_search.html/$',
    #    ArchiveIndexView.as_view(model=Article, date_field='pub_date'),
    #    name='display_search'),
    url(r'^login/login.html/$', views.LoginView.as_view(), name='login'),
    url(r'^new_user/new_user.html/$', views.NewUserView.as_view(), name='new_user'),
    url(r'^new_user/new_user_thanks.html/$', views.NewUserThanksView.as_view(), name='new_user_thanks')
]
