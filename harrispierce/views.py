# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import get_object_or_404, render, loader, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Q

from .forms import LoginForm, NewUserForm, SearchForm
from .models import Article, Journal, Section
from .views_functions import index_get, display_get


class NewUserView(generic.FormView):

    form_class = NewUserForm
    template_name = 'harrispierce/new_user/new_user.html'
    success_url = reverse_lazy('index_perso')

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            # create an object from the form but does not save it the db yet
            user = form.save(commit=False)

            #email =
            user_name = form.cleaned_data['user_name']
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

                    return redirect('index_perso')

        return render(request, self.template_name, {'form': form})


class LoginView(generic.FormView):

    form_class = LoginForm
    template_name = 'harrispierce/login/login.html'

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            # user exists or not
            user = authenticate(username=user_name, password=password)

            if user is not None:

                if user.is_active:
                    # user signified to system as logged in
                    login(request, user)
                    return redirect('index_perso')

        return render(request, self.template_name, {'form': form})


class IndexView(generic.ListView):   # ListView
    template_name = 'harrispierce/index.html'

    def get(self, request, **kwargs):
        journals, args = index_get()
        return render(request, self.template_name, args)


class DisplayView(generic.ListView):
    template_name = 'harrispierce/display.html'

    def get(self, request, **kwargs):
        if request.method == "GET":
            selection = request.GET.getlist("selection")
            if len(selection) == 0:
                return redirect('index')

            args = display_get(selection)

            return render(request, self.template_name, args)

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]


class IndexPersoView(LoginRequiredMixin, generic.ListView):
    template_name = 'harrispierce/login/index_perso.html'

    def get(self, request, **kwargs):
        journals, args = index_get()
        return render(request, self.template_name, args)


class DisplayPersoView(LoginRequiredMixin, generic.ListView):
    template_name = 'harrispierce/login/display_perso.html'

    def get(self, request, **kwargs):
        if request.method == "GET":
            selection = request.GET.getlist("selection")
            if len(selection) == 0:
                return redirect('index')

            args = display_get(selection)

            return render(request, self.template_name, args)


class SearchFormView(generic.FormView):
    form_class = SearchForm
    template_name = 'harrispierce/login/search_form.html'
    #template_name = 'harrispierce/shared/base_loggedin.html'
    success_url = reverse_lazy('display_search')


class DisplaySearchView(generic.ListView):
    form_class = SearchForm
    template_name = 'harrispierce/login/display_search.html'

    def get(self, request, **kwargs):
        if request.method == 'GET':
            form = SearchForm(request.GET)

            keyword = form['Keyword'].value()
            sources = form['Sources'].value()
            date = form['Date'].value()
            quantity = form['Quantity'].value()

            selection_dict = {}

            for journal in sources:

                articles = Article.objects.filter(
                    (Q(teaser__contains=keyword) | Q(title__contains=keyword)),
                    pub_date__gte=date,
                    journal_id__name=journal,
                ).order_by('pub_date')[:quantity]

                selection_dict[journal] = articles

            args = {'selection_dict': selection_dict}
            return render(request, self.template_name, args)


class MustBeLoggedInView(generic.ListView):
    model = Article
    template_name = 'harrispierce/must_be_loggedin.html'

