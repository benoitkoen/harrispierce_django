from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView
from . import views


urlpatterns = [
    url(r'^new_user/profile.html/$', views.ProfileView.as_view(), name='profile'),
]