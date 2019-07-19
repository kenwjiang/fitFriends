from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^/signup$', views.SignUpView.as_view(), name='signup'),
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),

]
print('URL route test')
