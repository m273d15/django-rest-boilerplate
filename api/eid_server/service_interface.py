from eid_server.models import ServiceRequest

def use_id():
    """
    This function is used by the eID-Service to initializes a new authentication session.
    The eID-Server responds with an unique session id which is sent to the eID-Client by
    the eID-Service. Using this session id the eID-Client can establish a connection with
    the eID-Server.
    """
    serviceRequest = ServiceRequest()
    serviceRequest.save()
    return serviceRequest.sessionId

def get_result(sessionId):
    """
    After the authentication session of eID-Client and eID-Server, the eID-Service can
    retrieve the result (in this case the restricted id) by calling this function. The
    required parameter is the session id which was provided by the initial call to use_id.
    """
    try:
        serviceRequest = ServiceRequest.objects.get(sessionId=sessionId)
    except ServiceRequest.DoesNotExist:
        return None
    return serviceRequest.restrictedId
