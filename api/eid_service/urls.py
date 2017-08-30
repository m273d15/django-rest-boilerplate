from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^init$', views.init),
    url(r'^getTcTokenUrl$', views.get_tc_token_url),
    url(r'^getTcToken$', views.get_tc_token),
    url(r'^refresh$', views.refresh),
    url(r'^error$', views.error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
