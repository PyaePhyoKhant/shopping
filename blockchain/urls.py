from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sell', views.sell, name='sell'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^block/(?P<pk>\d+)/', views.BlockDetail.as_view(), name='block_detail'),
]
