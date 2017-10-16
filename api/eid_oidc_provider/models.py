from django.db import models


class Registration(models.Model):

    name = models.CharField(max_length=100, default='')
    response_type = models.CharField(max_length=30)
    _redirect_uris = models.TextField(default='')
    date_created = models.DateField(auto_now_add=True)
    client_type = models.CharField(max_length=30, default='confidential')
    jwt_alg = models.CharField(max_length=10, default='RS256')
    contact_email = models.CharField(max_length=255, blank=True, default='')
    logo = models.CharField(max_length=255, blank=True, default='')
    terms_url = models.CharField(max_length=255, blank=True, default='')
    website_url = models.CharField(max_length=255, blank=True, default='')
    _post_logout_redirect_uris = models.TextField(blank=True, default='')
