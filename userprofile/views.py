from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import PinnedArticles

class PinView(generic.FormView):

    #form_class = PinForm
    #template_name = 'harrispierce/login/login.html'
    #success_url = reverse_lazy('index_perso')

    def post(self, request):

        if request.method == 'POST':

            user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
            journal = request.POST.get('journal')
            section = request.POST.get('section')
            article = request.POST.get('article')

            PinnedArticles.objects.create(
                user = user,
                journal = journal,
                section = section,
                article = article
            )

        return HttpResponse('')