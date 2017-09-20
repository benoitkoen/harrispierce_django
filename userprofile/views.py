from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

from harrispierce.models import Journal, Section, Article
from .models import PinnedArticles


class PinView(generic.FormView):

    #form_class = PinForm
    #template_name = 'harrispierce/login/login.html'
    #success_url = reverse_lazy('index_perso')

    def post(self, request):

        if request.method == 'POST':

            user = request.user
            journal_name = request.POST.get('journal')
            section_name = request.POST.get('section')
            article_pk = request.POST.get('article')

            journal = Journal.objects.get(name = journal_name)
            section = Section.objects.get(name = section_name)
            article = Article.objects.get(pk = article_pk)

            PinnedArticles.objects.create(
                user=user,
                journal=journal,
                section=section,
                article=article
            )

        return HttpResponse('')