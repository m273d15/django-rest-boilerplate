from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .utils.user import username_exists_in_db
from eid_service.openid_interface import get_user_id
from eid_service import views as eid_service_views


def open_id_auth(request):

    params = None
    if request.method == "GET":
        params = request.GET
    elif request.method == "POST":
        params = request.POST

    redirect_to = "%s?%s" % (reverse(eid_service_views.init), params.urlencode())
    return HttpResponseRedirect(redirect_to)


def open_id_login(request,
        redirect_field_name=REDIRECT_FIELD_NAME,
        current_app=None, extra_context=None):

    if request.method == "POST":
        return HttpResponseBadRequest()

    redirect_to = request.GET.get(redirect_field_name, '')

    if not is_safe_url(url=redirect_to, host=request.get_host()):
        return HttpResponseBadRequest()

    # we don't get the user_id from the request, but by calling an eID-service python-function

    user_id = get_user_id(request.GET.get('eid_access_token',''))

    if user_id == None:
        return HttpResponseBadRequest()

    if username_exists_in_db(user_id):
        user = User.objects.filter(username=user_id).first()
    else:
        user = User.objects.create_user(user_id)

    auth_login(request, user)

    return HttpResponseRedirect(redirect_to)
