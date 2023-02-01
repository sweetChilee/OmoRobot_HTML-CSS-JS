from django.contrib import admin
from django.urls import path
from .views import *

app_name = "omorobot"

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path("login/enterlogin/", enterlogin, name="enterlogin"),

    path("join/", join, name="join"),
    path("join/createuser/", create_user, name="createuser"),

    path("<str:pk>/createmycar/", create_mycar, name="create_mycar"),
    path("<str:fk>/deletemycar/<int:pk>/", delete_mycar, name="delete_mycar"),
    path("<str:pk>/createmycarset/", create_mycarset, name="create_mycarset"),

    path("<str:pk>/createmycarall/", create_mycarall, name="create_mycarall"),
    path("<str:fk>/deletemycarall/<int:pk>/", delete_allmycar, name="delete_mycarall"),

    path("select/", selectcar, name="selectcar"),

    path("select/chart/", chart, name="chart"),

    path("<str:pk>/", user, name="user"),
]
