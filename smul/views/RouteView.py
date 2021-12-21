from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from django.views.generic import RedirectView
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from ..serializers import ShurtSerializer, CounterSerializer

from ..models import Shurt
#@api_view(['GET'])
class RouteView(viewsets.GenericViewSet):
    queryset = Shurt.objects.all()
    serializer_class= ShurtSerializer
    serializer=ShurtSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Shurt,code=pk)
        #serializer = self.get_serializer(instance)
        #Response(serializer.data)
        return HttpResponseRedirect(redirect_to=instance.url)
    
    #def get_redirect_url(self, **kwargs):
    #    shurt = get_object_or_404(Shurt, code=kwargs["code"])
    #    return HttpResponseRedirect(redirect_to=shurt)