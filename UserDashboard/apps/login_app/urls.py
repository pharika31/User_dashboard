from django.conf.urls import url
from . import views
urlpatterns =[
 url(r'^$',views.index),
 url(r'^loginreg$',views.loginreg),
 url(r'^registration$',views.registration),
 url(r'^register$',views.register),
 url(r'^login$',views.login),
 url(r'^success$',views.success),
]
