from django.urls import path
from . import views

urlpatterns = [
    path('home',views.homefn,name="home"),
    path('register',views.regFun,name="register"),
    path('dashboard',views.dashfun,name="dashboard")
]
