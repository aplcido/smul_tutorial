from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view

from ..models import Shurt
@api_view(['GET'])
class RouteView(viewsets.ModelViewSet):
    def get_redirect_url(self, **kwargs):
        shurt = get_object_or_404(Shurt, code=kwargs["code"])
        return HttpResponseRedirect(redirect_to=shurt)