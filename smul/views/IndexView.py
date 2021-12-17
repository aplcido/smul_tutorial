from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, View

from ..forms import SmulForm
from ..models import Shurt

# Create your views here.
class IndexView(View):
    template_name = "smul/index.html"

    def get(self, request):
        return render(request, self.template_name, {"form": SmulForm()})

    def post(self, request):
       form = SmulForm(request.POST)
       if not form.is_valid():
           return render(request, self.template_name, {"form": form})
       domain = request.build_absolute_uri() #http://127.0.0.1:8000/ in this case
       smul = domain + Shurt.get_or_create_shurt(form.cleaned_data["url"]).code #encoded/shortened URL
       return render(request, self.template_name, {"form": form, "smul": smul})