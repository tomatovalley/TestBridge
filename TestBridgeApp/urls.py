
from django.conf.urls import url
from TestBridgeApp.views import RegisterUserView

urlpatterns = [url(r'register/',view=RegisterUserView.as_view(), name='register_view'),
]
