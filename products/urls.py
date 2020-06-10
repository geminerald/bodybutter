from django.conf.urls import url, include
from .views import products_view

urlpatterns = [
    url(r'^$', products_view, name='shop')
]

