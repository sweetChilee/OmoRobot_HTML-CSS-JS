from django.contrib import admin
from django.urls import path
from .views import *

app_name = "omorobot"

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path("login/enterlogin/", enterlogin, name="enterlogin"),

    path("join/", join, name="join"),
    path("createuser/", create_user, name="createuser"),

# 차트
    path("select/chart/", chart, name="chart"),

# pk루트 & 차 관련
    path("<str:pk>/createmycar/", create_mycar, name="create_mycar"),
    path("<str:fk>/deletemycar/<int:pk>/", delete_mycar, name="delete_mycar"),
    path("<str:pk>/createmycarset/", create_mycarset, name="create_mycarset"),

# pk루트 & 차트 관련
    path("<str:pk>/createmycarall/", create_mycarall, name="create_mycarall"),
    path("<str:fk>/deletemycarall/<int:pk>/", delete_allmycar, name="delete_mycarall"),

# 유저별
    path("<str:pk>/", user, name="user"),
]
