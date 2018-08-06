from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from .models import Endpoint
from .forms import EndpointForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .helpers import HelperClass
from django.db.models import Q


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


@method_decorator(csrf_exempt, name='dispatch')
class ApiResponse(View):

    def get(self, request, slug):
        endpoint_query_match = Endpoint.objects.filter(
                    Q(url=slug), Q(verb=request.method))
        body = HelperClass.helper_method_body(endpoint_query_match)
        is_json = len(request.build_absolute_uri().split('?'))
        response = HelperClass.helper_method_response(
            request, slug, is_json, endpoint_query_match, body)

        HelperClass.helper_method_logging(request, response, slug)

        return response

    def post(self, request, slug):
        body = helper_method_body(request.method, slug)
        is_json = len(request.build_absolute_uri().split('?'))
        endpoint_query_match = Endpoint.objects.filter(
            Q(url=slug), Q(verb=request.method))
        response = helper_method_response(
            request, slug, is_json, endpoint_query_match, body)

        print(helper_method_logging())
        print(helper_method_callback())

        return response
