"""
URL configuration for ebac_m13_bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import debug_toolbar
from ebac_m13_bookstore import views
from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

def home(request):
    return HttpResponse("🚀 EBAC Bookstore API está funcionando!", content_type="text/plain; charset=utf-8")

urlpatterns = [
    path('', home, name='home'),
    #path('__debug__/', include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("ebac_m13_bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("ebac_m13_bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path("update_server/", views.update_server, name="update_server"),
    path("hello/", views.hello_world, name="hello_world"),
]
