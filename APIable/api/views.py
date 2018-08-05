from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Welcome_View(TemplateView):
    template_name = 'api/index.html'
