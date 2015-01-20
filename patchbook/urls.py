from django.conf.urls import patterns, url
from patchbook import views

urlpatterns = patterns('',
  url(r'^patchset/new', views.patchset_create_or_update, name='patchset-create-or-update'),
  url(r'^$', views.index, name='index'),
)
