from uuid import UUID
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from eid_service.models import AuthenticationRequest


class HttpResponseRedirectEId(HttpResponseRedirect):
    """
    HTTP 302 Redirect response, where the destination may have protocol eid://.
    """

    def __init__(self, redirect_to, *args, **kwargs):
        self.allowed_schemes.append('eid')
        super().__init__(redirect_to, *args, **kwargs)



def get_tc_token_url(request):
    if request.method == 'GET':
        protocol = request.GET.get('protocol', 'http')
        host = request.GET.get('host', '127.0.0.1')
        if (protocol != 'http') and (protocol != 'eid'):
            return HttpResponseBadRequest()
        if (host != '127.0.0.1') and (host != 'localhost'):
            return HttpResponseBadRequest()
        ##
        # get sessionId from eID-Server
        ##
        authenticationRequest = AuthenticationRequest()
        authenticationRequest.save()
        tc_token_url = 'https://' + request.get_host() + '/api/eIdService/getTcToken?tcTokenId=' + str(authenticationRequest.tcTokenId)
        return HttpResponseRedirectEId(protocol + '://' + host + ':24727/eID-Client?tcTokenUrl=' + tc_token_url)
    else:
        return HttpResponseBadRequest()

def get_tc_token(request):
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
        ##
        # get result from eID-Server
        ##
        return HttpResponse("result from eID-Server")
    else:
        return HttpResponseBadRequest()
    return HttpResponseBadRequest()
    
def error(request):
    return HttpResponse("An error occurred during the authentication.")
