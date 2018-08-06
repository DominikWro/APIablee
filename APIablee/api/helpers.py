from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Endpoint
import logging
from django.core import serializers
import json


class HelperClass:
    @staticmethod
    def helper_method_body(endpoint_query_match):
        try:
            body = endpoint_query_match.values()[0]['body']

        except LookupError:
            body = {'body': 'not defined'}

        return body

    @staticmethod
    def helper_method_response(
            request, slug, is_json, endpoint_query_match, body):
        try:
            response_code = endpoint_query_match.values()[0]['response_code']
            charset = endpoint_query_match.values()[0]['encoding']
            print(charset)
            content_type = endpoint_query_match.values()[0]['content_type']
        except LookupError:
            response = JsonResponse({'Endpoint': 'Not Available'})

        if is_json == 2 and endpoint_query_match:
            response = HttpResponse(
                json.dumps(body, ensure_ascii=False),
                status=response_code,
                charset=charset,
                content_type="application/json")

            return response

        elif endpoint_query_match:
            response = HttpResponse(
                body.encode(charset),
                status=response_code,
                charset=charset,
                content_type=content_type)

        return response

    @staticmethod
    def helper_method_logging(request, response, slug):
        logging.basicConfig(
            filename='file.log',
            format='%(asctime)s %(message)s',
            level=logging.INFO)
        logging.info('INFO {0} {1} {2} {3} {4}'.format(
            slug,
            request.method,
            response.status_code,
            response.charset,
            response.content))

        return True

    @staticmethod
    def helper_method_callback():
        # TODO
        return True
