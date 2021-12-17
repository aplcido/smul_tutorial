from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView

from ..models import Shurt
class RouteView(RedirectView):
    def get_redirect_url(self, **kwargs):
        shurt = get_object_or_404(Shurt, code=kwargs["code"])
        return shurt.url 