from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^pin/$', views.PinView.as_view(), name='pin'),
    url(r'^like/$', views.LikeView.as_view(), name='like'),
]