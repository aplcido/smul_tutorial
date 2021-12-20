from re import template
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, View
from rest_framework import generics
from rest_framework import viewsets, mixins
from rest_framework.viewsets import ViewSetMixin
from django.http import HttpResponseRedirect

from ..forms import SmulForm
from ..models import Shurt
from ..serializers import ShurtSerializer, CounterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
#@api_view(['GET', 'POST'])
class IndexView(viewsets.ModelViewSet):
    template_name = "smul/index.html"
    queryset = Shurt.objects.all()
    serializer_class= ShurtSerializer
    serializer=ShurtSerializer

    
    
    def create(self, request, *args, **kwargs):
        
        
        response = super(IndexView, self).create(request, *args, **kwargs)
        
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        return HttpResponseRedirect(redirect_to='https://google.com')
    
    #def list():

    def get(self, request):
        #shurts = Shurt.objects.all()
        #serializer = ShurtSerializer(shurts, many=True)
        #return Response(self.serializer.data,template_name=self.template_name,content_type=SmulForm())
        return render(request, self.template_name, {"form": SmulForm()})

    #def post(self, request):
       #form = SmulForm(request.POST)
       #if not form.is_valid():
       #    return render(request, self.template_name, {"form": form})
       #domain = request.build_absolute_uri() #http://127.0.0.1:8000/ in this case
       #smul = domain + Shurt.get_or_create_shurt(form.cleaned_data["url"]).code #encoded/shortened URL
       #return render(request, self.template_name, {"form": form, "smul": smul})