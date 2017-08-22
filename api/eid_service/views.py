from uuid import UUID
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from eid_service.models import AuthenticationRequest
from eid_server.service_interface import use_id, get_result


class HttpResponseRedirectEId(HttpResponseRedirect):
    """
    HTTP 302 Redirect response, where the destination may have protocol eid://.
    """

    def __init__(self, redirect_to, *args, **kwargs):
        self.allowed_schemes.append('eid')
        super().__init__(redirect_to, *args, **kwargs)

def init(request):
    """
    Entrypoint for the authentication start with the eID-Service. Redirects to
    the Client-Checker preserving GET parameters.
    """
    if request.method == 'GET':
        return HttpResponseRedirect('/check?' + request.GET.urlencode())
    else:
        return HttpResponseBadRequest()

def get_tc_token_url(request):
    """
    Depending on the given arguments this view redirects the user agent to
    the eID-Client. It is possible to specifiy the protocol (http or eid) and
    the host (localhost or 127.0.0.1) of the redirect url via GET. Otherwise
    the default configuration is used. The redirect url contains the required
    GET parameter tcTokenUrl which contains a link to the tc token. A call to
    this view also prepares the session between eID-Client and eID-Server.
    """
    if request.method == 'GET':
        protocol = request.GET.get('protocol', 'http')
        host = request.GET.get('host', '127.0.0.1')
        if (protocol != 'http') and (protocol != 'eid'):
            return HttpResponseBadRequest()
        if (host != '127.0.0.1') and (host != 'localhost'):
            return HttpResponseBadRequest()
        openidParameter = request.GET.copy()
        if openidParameter.__contains__('protocol'):
            openidParameter.pop('protocol')
        if openidParameter.__contains__('host'):
            openidParameter.pop('host')
        authenticationRequest = AuthenticationRequest()
        authenticationRequest.sessionId = use_id()
        authenticationRequest.openidParameter = openidParameter.urlencode()
        authenticationRequest.save()
        tc_token_url = 'https://' + request.get_host() + '/api/eIdService/getTcToken?tcTokenId=' + str(authenticationRequest.tcTokenId)
        return HttpResponseRedirectEId(protocol + '://' + host + ':24727/eID-Client?tcTokenUrl=' + tc_token_url)
    else:
        return HttpResponseBadRequest()

def get_tc_token(request):
    """
    Returns a xml-based tc token providing the required information to set up
    the authentication session between eID-Client and eID-Server. The required
    GET parameter tcTokenId identifies from an earlier call to get_tc_token_url.
    """
    if request.method == 'GET':
        try:
            tcTokenId = UUID(request.GET.get('tcTokenId'))
        except ValueError:
            return HttpResponseBadRequest()
        except TypeError:
            return HttpResponseBadRequest()
        try:
            authenticationRequest = AuthenticationRequest.objects.get(tcTokenId=tcTokenId)
        except AuthenticationRequest.DoesNotExist:
            return HttpResponseBadRequest()
        context = {
            'serverAddress': 'https://' + request.get_host() + '/api/eID',
            'sessionId': str(authenticationRequest.sessionId),
            'refreshAddress': 'https://' + request.get_host() + '/api/eIdService/refresh?refreshId=' + str(authenticationRequest.refreshId),
            'communicationErrorAddress': 'https://' + request.get_host() + '/api/eIdService/error',
        }
        return render(request, 'tcTokenTemplate.xml', context, content_type = 'application/xml')
    else:
        return HttpResponseBadRequest()

def refresh(request):
    """
    After a successful authentication session between eID-Client and eID-Server the
    eID-Client redirects the user agent to this view specified in the tc token. It
    fetches the result from the eID-Server and returns an access token as json providing
    access to the user id by calling get_user_id.
    """
    if request.method == 'GET':
        try:
            refreshId = UUID(request.GET.get('refreshId'))
        except ValueError:
            return HttpResponseBadRequest()
        except TypeError:
            return HttpResponseBadRequest()
        try:
            authenticationRequest = AuthenticationRequest.objects.get(refreshId=refreshId)
        except AuthenticationRequest.DoesNotExist:
            return HttpResponseBadRequest()
        authenticationRequest.restrictedId = get_result(authenticationRequest.sessionId)
        authenticationRequest.save()
        return HttpResponseRedirect('https://' + request.get_host() + '/api/openid/login?eid_access_token=' + str(authenticationRequest.accessToken) + "&" + authenticationRequest.openidParameter)
    else:
        return HttpResponseBadRequest()
    
def error(request):
    """
    The user agent is redirected to this view if the authentication session between eID-Client
    and eID-Server fails.
    """
    return HttpResponseRedirect('https://' + request.get_host() + '/api/openid/login')
