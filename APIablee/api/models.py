from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Endpoint(models.Model):
    VERB_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
    )

    CONTENT_TP_CHOICES = (
        ('text/plain', 'text/plain'),
        ('text/html', 'text/html'),
        ('application/json', 'application/jsonT'),
    )

    ENCODING_CHOICES = (
        ('UTF-8', 'UTF-8'),
        ('UTF-16', 'UTF-16'),
        ('ISO-8859-1', 'ISO-8859-1'),
    )

    url = models.CharField(max_length=100)
    verb = models.CharField(max_length=5, choices=VERB_CHOICES)
    response_code = models.CharField(max_length=100)
    content_type = models.CharField(max_length=17, choices=CONTENT_TP_CHOICES)
    encoding = models.CharField(max_length=10, choices=ENCODING_CHOICES)
    body = models.CharField(max_length=1000, blank=True)
    external_service_address = models.CharField(max_length=100, blank=True)
    external_service_login = models.CharField(max_length=100, blank=True)
    external_service_token = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.url
        return self.verb
        return self.response_code
        return self.content_type
        return self.encoding
        return self.body
