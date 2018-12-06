
from django.conf.urls import url
from TestBridgeApp.views import RegisterUser

urlpatterns = [
     url(r'register/',RegisterUser, name='register_user'),
]
