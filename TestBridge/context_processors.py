from __future__ import unicode_literals

from Users.models import Tb_user
from Devices.models import Device
from Projects.models import Project

def variables(request):
    if request.user.is_authenticated():
        user = Tb_user.objects.get(username=request.user)
        return {
            'userInfo': user,
        }
    else:
        return {
            'userInfo': None
        }