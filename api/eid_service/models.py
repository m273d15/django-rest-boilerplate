import uuid
from django.db import models

class AuthenticationRequest(models.Model):
    """
    This model stores information about authentication requests to the eID-Service.
    """
    tcTokenId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sessionId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    refreshId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    accessToken = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    restrictedId = models.BinaryField()
    openidParameter = models.TextField()
