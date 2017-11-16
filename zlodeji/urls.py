from django.urls import path, re_path

from . import views

app_name = 'zlodej'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'login/$', views.LogInView.as_view(), name='login'),
    re_path(r'logout/$', views.LogOutView.as_view(), name='logout'),
    re_path(r'zlodejs/$', views.ZlodejsView.as_view(), name='zlodejs'),
    re_path(r'zlodej/add/$', views.ZlodejCreate.as_view(), name='zlodej-add'),
    re_path(r'zlocin/add/$', views.ZlocinCreate.as_view(), name='zlocin-add'),
    re_path(r'urobil/add/$', views.UrobilCreate.as_view(), name='urobil-add'),
    re_path(r'zlocin/(?P<pk>[0-9]+)/?$', views.DetailView.as_view(), name='zlocin-detail'),
    # /music/album/add/
    re_path(r'zlodej/(?P<pk>[a-zA-Z]+)/$', views.ZlodejUpdate.as_view(), name='zlodej-update'),
    re_path(r'zlocin/(?P<pk>[0-9]+)/$', views.ZlocinUpdate.as_view(), name='zlocin-update'),
    re_path(r'urobil/(?P<pk>[a-zA-Z]+)/$', views.UrobilUpdate.as_view(), name='urobil-update'),

    re_path(r'zlodej/(?P<pk>[a-zA-Z]+)/delete/$', views.ZlodejDelete.as_view(), name='zlodej-delete'),

]
