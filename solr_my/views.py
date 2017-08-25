#!/usr/bin/env python
# encoding: utf-8

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

#@api_view(('GET',))
#@permission_classes((AllowAny,))
#def api_root(request, format=None):
#    api_root = {}
#    api_root['search'] = reverse('search', request=request)
#    #api_root['auth'] = reverse('auth', request=request)
#    return Response(api_root)
