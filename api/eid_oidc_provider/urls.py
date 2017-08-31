from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^login/$', views.open_id_login, name='login'),
    url(r'^logout/$', auth_views.logout, { 'next_page': '/' }, name='logout'),
    url(r'^auth/$', views.open_id_auth, name="auth"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
