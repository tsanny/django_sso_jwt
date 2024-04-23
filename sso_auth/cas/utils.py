import os

from django.conf import settings as django_settings
from .client import CASClient
from urllib import parse

module_dir = os.path.dirname(__file__)  # get current directory

def get_cas_client(service_url=None, request=None):
    server_url = django_settings.SSO_UI_URL
    if server_url and request and server_url.startswith("/"):
        scheme = request.META.get("X-Forwarded-Proto", request.scheme)
        server_url = scheme + "://" + request.META["HTTP_HOST"] + server_url

    return CASClient(service_url=service_url, server_url=server_url, version=2)

def get_protocol(request):
    if request.is_secure() or django_settings.SSO_UI_FORCE_SERVICE_HTTPS:
        return "https"

    return "http"

def get_service_url(request, redirect_to=None):
    protocol = get_protocol(request)
    host = request.get_host()
    service = parse.urlunparse(
        (protocol, host, request.path, "", "", ""))

    return service

def get_logout_url(request):
    service_url = get_service_url(request)
    client = get_cas_client(service_url)
    return client.get_logout_url()
