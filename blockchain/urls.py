from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sell', views.sell, name='sell'),
    url(r'^message', views.message, name='message'),
    url(r'^info', views.info, name='info'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^block/(?P<pk>\d+)/', views.block_detail, name='block_detail'),
]
