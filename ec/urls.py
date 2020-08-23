from django.contrib import admin
from django.urls import path

import catalogue.views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products/<int:product_id>/', catalogue.views.product_detail,
    #      name='product_detail'),
    path('', catalogue.views.product_list, name='product_list'),
]
