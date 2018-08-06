from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name="welcome"),
    path('endpoint/list', views.EndpointList.as_view(), name='endpoint_list'),
    path('endpoint/new', views.CreateEndpoint.as_view(), name='endpoint_new'),
    path('<path:slug>', views.ApiResponse.as_view()),
]
