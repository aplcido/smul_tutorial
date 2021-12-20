"""smul_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from smul import views
from smul.views import IndexView, RouteView
from rest_framework.routers import DefaultRouter

#route_url = RouteView.as_view({
#    'get': 'retrieve',
#})


# Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'url', RouteView)
#router.register(r'users', views.UserViewSet)



# Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'smul', views.IndexView)

app_name = 'smul'
urlpatterns = [
    path('', IndexView.as_view({'get': 'get','post':'create'}), name='index'),
    path("<str:code>", RouteView, name="route"),
    path('admin/', admin.site.urls),
 #   path('', include(router.urls)),
]
