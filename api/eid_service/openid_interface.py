from uuid import UUID
from eid_service.models import AuthenticationRequest


def get_user_id(accessToken):
    """
    Given a valid access token this view returns the user id retieved during an
    authentication session between eID-Client and eID-Server.
    """
    try:
        authenticationRequest = AuthenticationRequest.objects.get(accessToken=accessToken)
    except AuthenticationRequest.DoesNotExist:
        return None
    return str(authenticationRequest.restrictedId)
