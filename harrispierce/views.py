# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from harrispierce.forms import LoginForm, NewUserForm, SearchForm

from .models import Article, Journal, Section, User


class IndexView(generic.ListView):   # ListView
    template_name = 'harrispierce/index.html'

    def get_queryset(self):
        return Journal.objects.all()

    context_object_name = 'latest_question_list'


class DisplayView(generic.ListView):
    model = Article
    template_name = 'harrispierce/display.html'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]


"""
class DisplayView(generic.DayArchiveView):
    model = Article
    template_name = 'harrispierce/display_search.html'

    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]
"""


class LoginView(generic.FormView):
    model = User
    form_class = LoginForm
    template_name = 'harrispierce/login/login.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed. # It should return an HttpResponse.
        # form.send_email()
        return  # super(ContactView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class IndexPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/index_perso.html'


class DisplayPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/display_perso.html'


class SearchFormView(generic.FormView):
    model = Article
    form_class = SearchForm
    template_name = 'harrispierce/login/search_form.html'


class DisplaySearchView(generic.FormView):
    model = Article
    form_class = SearchForm
    template_name = 'harrispierce/login/display_search.html'


class NewUserView(generic.FormView):
    model = User
    form_class = NewUserForm
    template_name = 'harrispierce/new_user/new_user.html'
