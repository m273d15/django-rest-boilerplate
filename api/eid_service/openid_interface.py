from uuid import UUID
from django.core.exceptions import ValidationError
from eid_service.models import AuthenticationRequest


def get_user_id(accessToken):
    """
    Given a valid access token this view returns the user id retrieved during an
    authentication session between eID-Client and eID-Server.
    """
    try:
        authenticationRequest = AuthenticationRequest.objects.get(accessToken=accessToken)
    except (AuthenticationRequest.DoesNotExist, ValidationError):
        return None
    return str(authenticationRequest.restrictedId)
