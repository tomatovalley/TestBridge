from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def not_found(request):
    try:
        response = render_to_response('404.html', {})
    except Exception as e:
        print e
    response.status_code = 404
    return response