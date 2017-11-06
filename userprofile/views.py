from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, loader, redirect

from harrispierce.models import Journal, Section, Article
from .models import PinnedArticles, LikedArticles, SentArticles, Following
from .views_functions import profile_get, recommended_get


class PinView(generic.FormView):
    """
    A view that creates a PinnedArticles object when a user clicks on the pin badge under each article displayed.
    """

    def post(self, request):
        if request.method == 'POST':

            user = request.user
            article_pk = request.POST.get('article')

            article = Article.objects.get(pk = article_pk)

            PinnedArticles.objects.create(
                user=user,
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
            article_pk = request.POST.get('article')

            article = Article.objects.get(pk=article_pk)

            journal = article.journal
            section = article.section

            print('IN LIKE VIEW  ', user, journal.pk, section.pk, article_pk)

            LikedArticles.objects.create(
                user=user,
                article=article
            )

        return HttpResponse('')


class RemoveView(generic.FormView):
    """
    A view that creates a LikedArticles object when a user clicks on the like badge under each article displayed.
    """

    def post(self, request):
        if request.method == 'POST':
            user = request.user
            article_pk = request.POST.get('article')

            print('IN REMOVE VIEW', user.pk, article_pk)


            PinnedArticles.objects.get(
                article_id=article_pk,
                user_id=user.pk
            ).delete()

        return HttpResponse('')


class SendView(generic.FormView):
    """
    A view that creates a LikedArticles object when a user clicks on the like badge under each article displayed.
    """

    def post(self, request):
        print('#####################################')
        if request.method == 'POST':
            sender = request.user
            recipient_name = request.POST.get('recipient')
            comment = request.POST.get('comment')
            article_pk = request.POST.get('article')

            print('Trying to SEND:', recipient_name, article_pk, comment)

            recipient = User.objects.get(username=recipient_name)

            article = Article.objects.get(pk=article_pk)

            # throws a 500 error if either one of the relations is not found
            one_way_relation = Following.objects.get(follower_id=recipient.pk, user_followed_id=sender.pk)
            reciprocal_relation = Following.objects.get(follower_id=sender.pk, user_followed_id=recipient.pk)

            SentArticles.objects.create(
                sender=sender,
                recipient=recipient,
                comment = comment,
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

            # can't follow yourself
            if user != user_to_follow:
                Following.objects.create(
                    user_followed=user_to_follow,
                    follower=user,
                )

            else:
                raise ValueError('You cannot follow yourself.')

        return HttpResponse('')


class ProfileView(LoginRequiredMixin, generic.ListView):
    """
    A view that displays the profile information for a loggedin user.
    """
    template_name = 'userprofile/profile.html'

    def get(self, request, **kwargs):
        user = request.user
        args = profile_get(user)

        return render(request, self.template_name, args)


class RecommendedView(LoginRequiredMixin, generic.ListView):
    """
    A view that displays the articles recommended by a friend for a loggedin user.
    """
    template_name = 'userprofile/recommended.html'

    def get(self, request, **kwargs):
        user = request.user
        args = recommended_get(user)

        return render(request, self.template_name, args)