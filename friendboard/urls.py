from django.urls import path
from . import views

# 술친구 urls.py
app_name = 'friendboard'
urlpatterns = [
    path('', views.friendboard, name="friendboard"),
]
