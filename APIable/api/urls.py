from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Welcome_View.as_view(), name="welcome"),
    path('endpoint/list', views.Endpoint_List.as_view(), name='endpoint_list'),
    path('endpoint/new', views.Create_Endpoint.as_view(), name='endpoint_new'),
]
