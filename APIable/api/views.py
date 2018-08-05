from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Endpoint


# Create your views here.
class Welcome_View(TemplateView):
    template_name = 'api/index.html'


class Endpoint_List(View):
    def get(self, request):
        endpoints = Endpoint.objects.all()
        return render(
            request, 'api/endpoint_list.html', {'endpoints': endpoints})
