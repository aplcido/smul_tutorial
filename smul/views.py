from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, View

# Create your views here.
class IndexView(View):
    template_name = "smul/index.html"

    def get(self, request):
        return render(request, self.template_name)