import uuid
from django.db import models

class AuthenticationRequest(models.Model):
    tcTokenId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sessionId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    refreshId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
