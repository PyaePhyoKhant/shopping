from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^details', views.details, name='details'),
    url(r'^block/(?P<pk>\d+)/', views.BlockDetail.as_view(), name='block_detail'),
]
