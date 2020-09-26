from django.contrib import admin
from django.urls import path

import cart.views
import catalogue.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart.views.cart_list, name='cart_list'),
    path('cart/<int:product_id>/add/', cart.views.cart_add, name='cart_add'),

    path('products/<int:product_id>/', catalogue.views.product_detail, name='product_detail'),
    path('', catalogue.views.product_list, name='product_list'),
]
