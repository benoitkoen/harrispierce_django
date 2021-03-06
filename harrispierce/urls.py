from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^display.html/$', views.DisplayView.as_view(), name='display'),
    url(r'^login/index_perso.html/$', views.IndexPersoView.as_view(), name='index_perso'),
    url(r'^login/display_perso.html/$', views.DisplayPersoView.as_view(), name='display_perso'),
    url(r'^login/search_form.html/$', views.SearchFormView.as_view(), name='search_form'),
    url(r'^login/display_search.html/$', views.DisplaySearchView.as_view(), name='display_search'),
    url(r'^harrispierce/must_be_loggedin.html/$', views.MustBeLoggedInView.as_view(), name='must_be_loggedin'),
    url(r'^login/login.html/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^new_user/new_user.html/$', views.NewUserView.as_view(), name='new_user'),
    url(r'^new_user/thanks.html/$', views.ThanksView.as_view(), name='thanks'),
]

