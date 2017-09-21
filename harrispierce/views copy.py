# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import get_object_or_404, render, loader, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Q

from .forms import LoginForm, NewUserForm, SearchForm
from .models import Article, Journal, Section
from .views_functions import index_get, display_get, display_search


class NewUserView(generic.FormView):

    form_class = NewUserForm
    template_name = 'harrispierce/new_user/new_user.html'
    success_url = reverse_lazy('index_perso')

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

    def get(self, request):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {'form': form})


class ThanksView(generic.ListView):
    template_name = 'harrispierce/new_user/thanks.html'
    success_url = reverse_lazy('thanks')


class LoginView(generic.FormView):

    form_class = LoginForm
    template_name = 'harrispierce/login/login.html'
    success_url = reverse_lazy('index_perso')

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


class LogoutView(generic.RedirectView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class IndexView(generic.ListView):   # ListView
    template_name = 'harrispierce/index.html'

    def get(self, request, **kwargs):
        args = index_get(None)
        return render(request, self.template_name, args)


class DisplayView(generic.ListView):
    template_name = 'harrispierce/display.html'

    def get(self, request, **kwargs):
        if request.method == "GET":
            selection = request.GET.getlist("selection")
            if len(selection) == 0:
                return redirect('index')

            args = display_get(selection, None)

            return render(request, self.template_name, args)

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]


class IndexPersoView(LoginRequiredMixin, generic.ListView):
    template_name = 'harrispierce/login/index_perso.html'

    def get(self, request, **kwargs):

        user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user

        args = index_get(user)

        return render(request, self.template_name, args)


class DisplayPersoView(LoginRequiredMixin, generic.ListView):
    template_name = 'harrispierce/login/display_perso.html'

    def get(self, request, **kwargs):
        if request.method == "GET":
            selection = request.GET.getlist("selection")
            if len(selection) == 0:
                return redirect('index')

            user = request.user._wrapped if hasattr(request.user,'_wrapped') else request.user

            args = display_get(selection, user)

            return render(request, self.template_name, args)


class SearchFormView(generic.FormView):
    form_class = SearchForm
    template_name = 'harrispierce/login/search_form.html'
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
            quantity = int(form['Quantity'].value())

            args = display_search(keyword, sources, date, quantity)
            print(args)

            return render(request, self.template_name, args)


class MustBeLoggedInView(generic.ListView):
    model = Article
    template_name = 'harrispierce/must_be_loggedin.html'

