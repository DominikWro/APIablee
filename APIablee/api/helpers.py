from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Endpoint

class HelperClass:
    @staticmethod
    def helper_method_body(endpoint_query_match):
        try:
            body = endpoint_query_match.values()[0]['body']

        except:
            body = {'body': 'not defined'}

        return body

    @staticmethod
    def helper_method_response(
            request, slug, is_json, endpoint_query_match, body):
        try:
            response_code = endpoint_query_match.values()[0]['response_code']
            charset = endpoint_query_match.values()[0]['encoding']
            content_type = endpoint_query_match.values()[0]['content_type']
        except:
            response = JsonResponse({'Endpoint': 'Not Available'})

        if is_json == 2 and endpoint_query_match:
            response = HttpResponse("%s" % body.encode('utf-16'))
            print('json')

        elif endpoint_query_match:
            # print(body)
            response = HttpResponse(
                body.encode(charset),
                status=response_code,
                charset=charset,
                content_type=content_type)
            # print(endpoint_query_match.values()[0]['response_code'])

        return response

    @staticmethod
    def helper_method_logging(request, response, slug):
        print(
            'INFO',
            timezone.now(),
            slug,
            request.method,
            response.status_code,
            response.charset,
            response.content)
        return "Logging"

    @staticmethod
    def helper_method_callback():
        return True
