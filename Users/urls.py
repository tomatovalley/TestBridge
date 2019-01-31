from django.conf.urls import url
from Users import views
from django.views.generic import TemplateView

urlpatterns = [
   url(r'^register/$', views.UserRegister.as_view(), name='user_register'),
   url(r'^register/success/$', TemplateView.as_view(template_name="Users/registration_success.html"), name = 'register_success'),
   url(r'^profile/(?P<username>\w{1,50})/$',views.user_edit, name='user_profile'),
   url(r'^delete/(?P<username>\w{1,50})/$',views.user_delete, name='user_delete'),
]