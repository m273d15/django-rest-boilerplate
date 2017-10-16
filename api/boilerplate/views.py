from django.contrib.auth.models import User, Group
from django.contrib import messages
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponseRedirect
from datetime import date
from subprocess import run
from eid_oidc_provider.models import Registration
from django.core.mail import send_mail


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def registration(request):
    """
    Insert client data into public database 'registration' and
    send email to hardcoded administrator.
    """

    email = request.GET.get('email','')

    r = Registration(
        name = request.GET.get('clientName',''),
        client_type = request.GET.get('clientType',''),
        response_type = request.GET.get('responseType','id_token token'),
        _redirect_uris = request.GET.get('redirectURIs',''),
        jwt_alg = request.GET.get('jwt','RS256'),
        contact_email = email,
        website_url = request.GET.get('website',''),
        terms_url = request.GET.get('terms',''),
        logo = request.GET.get('logo',''),
        _post_logout_redirect_uris = request.GET.get('logout','')
    )
    r.save()

    """ TODO:
    configure mail server with smtplib module
    https://docs.djangoproject.com/en/1.11/topics/email/
    """
    """
    send_mail(
    '[eid_provider] New Client Registration',
    'There is a new client registration pending.',
    email,
    ['eidadmin@example.com'],
    fail_silently=True,
    )
    """

    return HttpResponseRedirect("/registration/")
