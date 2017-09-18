from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm



class ProfileView(generic.FormView):

    template_name = 'userprofile/profile.html'

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
"""
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('profile')
        else:
            user = request.user

            # trigger Userprofile property in Models
            profile = user.profile
            form = UserProfileForm(instance=profile)

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('profile.html', args)
"""