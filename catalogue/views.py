from django.http import Http404
from django.template.response import TemplateResponse
from catalogue.models import Product


def product_list(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request, 'catalogue/product_list.html',
                            {'products': products})

# def product_detail(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         raise Http404
#     return TemplateResponse(request, 'catalogue/product_detail.html',
#                             {'product': product})