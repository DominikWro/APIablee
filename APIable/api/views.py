from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from .models import Endpoint
from .forms import EndpointForm


# Create your views here.
class Welcome_View(TemplateView):
    template_name = 'api/index.html'


class Endpoint_List(View):
    def get(self, request):
        endpoints = Endpoint.objects.all()
        return render(
            request, 'api/endpoint_list.html', {'endpoints': endpoints})


class Create_Endpoint(FormView):
    template_name = 'api/endpoint_edit.html'
    success_url = '/endpoint/success'
    form_class = EndpointForm

    def form_valid(self, form):
        self.object = form.save()
        return super(Create_Endpoint, self).form_valid(form)
