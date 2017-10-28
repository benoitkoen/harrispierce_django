from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^pin/$', views.PinView.as_view(), name='pin'),
    url(r'^like/$', views.LikeView.as_view(), name='like'),
    url(r'^send/$', views.SendView.as_view(), name='send_form'),
    url(r'^follow/$', views.FollowView.as_view(), name='follow'),
    url(r'^profile.html/$', views.ProfileView.as_view(), name='profile')
]