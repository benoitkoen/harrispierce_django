# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic

from .models import Article, Journal, Section, User


class IndexView(generic.ListView):
    template_name = 'harrispierce/index.html'
    context_object_name = 'latest_question_list'


class DisplayView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/display.html'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]

    
class LoginView(generic.DetailView):
    model = User
    template_name = 'harrispierce/login/login.html'


class IndexPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/index_perso.html'


class DisplayPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/display_perso.html'


class DisplaySearchView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/display_search.html'


class NewUserView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/new_user/new_user.html'
