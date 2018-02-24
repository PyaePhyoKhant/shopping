"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import blockchain.api_views as block_api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blockchain.views import login_view, signup_view

router = DefaultRouter()
router.register(r'block', block_api.BlockViewSet, base_name='block')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('blockchain.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login_view'),
    url(r'^signup/', signup_view, name='signup_view'),
]

urlpatterns += staticfiles_urlpatterns()
