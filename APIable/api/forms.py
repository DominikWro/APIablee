from django import forms
from .models import Endpoint


class EndpointForm(forms.ModelForm):

    class Meta:
        model = Endpoint
        fields = (
            'url',
            'verb',
            'response_code',
            'content_type',
            'encoding',
            'body',
            'external_service_address',
            'external_service_login',
            'external_service_token')
