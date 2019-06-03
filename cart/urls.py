from django.conf.urls import url
from .views import add_to_cart, view_cart, remove_from_cart,remove_all_from_cart
urlpatterns = [
    url(r'^add_to_cart/(?P<id>\d+)$', add_to_cart, name='add_to_cart_link'),
    url(r'^remove_from_cart/(?P<id>\d+)$', remove_from_cart, name='remove_from_cart_link'),
    url(r'^view_cart/$', view_cart),
    url(r'^clear_cart/$', remove_all_from_cart, name='remove_all_from_cart_link')
]