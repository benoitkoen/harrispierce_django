from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

from harrispierce.models import Journal, Section, Article
from .models import PinnedArticles, LikedArticles


class PinView(generic.FormView):

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