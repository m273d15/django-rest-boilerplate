import uuid
from django.db import models

class ServiceRequest(models.Model):
    """
    This model stores information about the authentication session between eID-Service
    and eID-Server. The sessionId identifies the session. The restrictedId is the result
    of the authentication between eID-Server and the electronic identity meaning the
    user id.
    """
    sessionId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    restrictedId = models.BinaryField()
