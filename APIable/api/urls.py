from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Welcome_View.as_view(), name="welcome"),
]
