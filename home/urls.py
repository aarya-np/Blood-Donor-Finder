from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("index",views.index, name='home'),
    path("donorlist",views.donorlist, name='donorlist'),
     path("bloodbanks",views.bloodbanks, name='bloodbanks'),
 path("registration",views.registration, name='registration'),
 path("donatenow",views.donatenow, name='donatenow'),
 path("bloodbanklogin",views.bloodbanklogin, name='bloodbanklogin'),
  path("bhaktapurbb",views.bhaktapurbb, name='bhaktapurbb'),
  path("changedata",views.changedata, name='changedata'),
  path("cbtc",views.cbtc, name='cbtc'),
  path("tuh",views.tuh, name='tuh'),
] 