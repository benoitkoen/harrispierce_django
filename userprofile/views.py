from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, loader, redirect

from harrispierce.models import Journal, Section, Article
from .models import PinnedArticles, LikedArticles, Following
from .views_functions import profile_get


class PinView(generic.FormView):
    """
    A view that creates a PinnedArticles object when a user clicks on the pin badge under each article displayed.
    """

    def post(self, request):
        if request.method == 'POST':

            user = request.user
            journal_pk = request.POST.get('journal')
            section_pk = request.POST.get('section')
            article_pk = request.POST.get('article')

            journal = Journal.objects.get(pk = journal_pk)
            section = Section.objects.get(pk = section_pk)
            article = Article.objects.get(pk = article_pk)

            PinnedArticles.objects.create(
                user=user,
                journal=journal,
                section=section,
                article=article
            )

        return HttpResponse('')


class LikeView(generic.FormView):
    """
    A view that creates a LikedArticles object when a user clicks on the like badge under each article displayed.
    """

    def post(self, request):
        if request.method == 'POST':
            user = request.user
            journal_pk = request.POST.get('journal')
            section_pk = request.POST.get('section')
            article_pk = request.POST.get('article')

            journal = Journal.objects.get(pk=journal_pk)
            section = Section.objects.get(pk=section_pk)
            article = Article.objects.get(pk=article_pk)

            LikedArticles.objects.create(
                user=user,
                journal=journal,
                section=section,
                article=article
            )

        return HttpResponse('')


class FollowView(generic.FormView):
    """
    A view that creates a Following object when a user fills in the follow form.
    """
    def post(self, request):
        if request.method == 'POST':
            user = request.user
            user_to_follow = request.POST.get('user_to_follow')

            user_to_follow = User.objects.get(username=user_to_follow)

            Following.objects.create(
                user_followed=user_to_follow,
                follower=user,
            )

        return HttpResponse('')


class ProfileView(generic.FormView):
    """
    A view that displays the articles according to the journals and sections choice for a loggedin user.
    """
    template_name = 'userprofile/profile.html'

    def get(self, request, **kwargs):
        user = request.user
        args = profile_get(user)

        return render(request, self.template_name, args)