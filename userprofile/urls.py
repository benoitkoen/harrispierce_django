from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView
from . import views


urlpatterns = [
    url(r'^pin/$', views.PinView.as_view(), name='pin'),
]