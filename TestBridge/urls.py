"""TestBridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, handler404
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static

handler404='TestBridge.views.not_found'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('Users.urls', namespace='usersapp')),
    url(r'^', include('TestBridgeApp.urls', namespace='testbridgeapp')),

    url(r'^api-auth/', include('rest_auth.urls')),
    url(r'^api-devices/', include('Devices.urls')),
    url(r'^api-projects/', include('Projects.urls')),

    url(r'^projects/', include('Projects.urls',namespace='projects')),
    url(r'^devices/', include('Devices.urls',namespace='devices')),
    url(r'^tests/', include('Tests.urls',namespace='tests')),
    url(r'^bugs/', include('Bugs.urls',namespace='bugs')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)