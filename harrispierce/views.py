# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, loader, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
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
    success_url = reverse_lazy('index')

    """
    def get(self, request):
        print('AJLKJHLKDJAS')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    """

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            #user = form.save(commit=False)
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            # user exists or not
            user = authenticate(username=user_name, password=password)

            if user is not None:

                if user.is_active:
                    # user signified to system as logged in
                    login(request, user)
                    return redirect('index_perso')#index_perso

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class IndexPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/index_perso.html'


@login_required(login_url='login')
class DisplayPersoView(generic.DetailView):
    model = Article
    template_name = 'harrispierce/login/display_perso.html'


class SearchFormView(generic.FormView):
    model = Article
    form_class = SearchForm
    template_name = 'harrispierce/login/search_form.html'
    success_url = reverse_lazy('display_search')


class DisplaySearchView(generic.ListView):
    model = Article
    form_class = SearchForm
    template_name = 'harrispierce/login/display_search.html'


class NewUserView(generic.FormView):

    model = User
    form_class = NewUserForm
    template_name = 'harrispierce/new_user/new_user.html'
    success_url = reverse_lazy('new_user_thanks')

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user_name = form.cleaned_data['user_name']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.username = user_name
            user.email = request.POST['email']
            user.set_password(password)
            user.save()

            # user exists or not
            user = authenticate(username=user_name, password=password)

            if user is not None:

                if user.is_active:
                    # user signified to system as logged in
                    login(request, user)
                    return redirect('new_user_thanks')#('index_perso')

        return render(request, self.template_name, {'form': form})


class NewUserThanksView(generic.ListView):

    model = Article
    template_name = 'harrispierce/new_user/new_user_thanks.html'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]

