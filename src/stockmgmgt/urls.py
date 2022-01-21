from django.urls import path, re_path
from .views import Liststock, DetailStock


urlpatterns = [
   re_path(r'^stocks$', Liststock.as_view(), name='lista-stock'),
   re_path(r'^stocks/(?P<pk>[0-9]+)$', DetailStock.as_view(), name='detail-stock'),
]