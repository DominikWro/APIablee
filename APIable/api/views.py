from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from .models import Endpoint
from .forms import EndpointForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'api/index.html'


class EndpointList(View):
    def get(self, request):
        endpoints = Endpoint.objects.all()
        return render(
            request, 'api/endpoint_list.html', {'endpoints': endpoints})


class SuccessView(TemplateView):
    template_name = 'api/success.html'


class CreateEndpoint(FormView):
    template_name = 'api/endpoint_edit.html'
    success_url = '/endpoint/new'
    form_class = EndpointForm

    def form_valid(self, form):
        self.object = form.save()
        return super(CreateEndpoint, self).form_valid(form)
