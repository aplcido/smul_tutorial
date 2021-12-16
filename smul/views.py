from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, View
from .forms import SmulForm

# Create your views here.
class IndexView(View):
    template_name = "smul/index.html"

    def get(self, request):
        return render(request, self.template_name, {"form": SmulForm()})

    def post(self, request):
       form = SmulForm(request.POST)
       smul="teste"
       if not form.is_valid():
           return render(request, self.template_name, {"form": form})
       return render(request, self.template_name, {"form": form, "smul": smul})    