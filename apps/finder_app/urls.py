from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^finder$', views.finder),
    url(r'^gym/(?P<place_id>[a-zA-Z0-9._-]+)$', views.gym_page),
    url(r'^gym/(?P<place_id>[a-zA-Z0-9._-]+)/set$', views.set_gym_default),
    url(r'^preference$', views.pref_form_page),
    url(r'^preference/submit$', views.pref_form_submit),
]
