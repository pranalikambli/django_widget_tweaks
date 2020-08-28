from django.views.generic import CreateView

from .models import Products


class BasicProductView(CreateView):
    model = Products

    template_name = 'basic_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/basic_product"


class TweakProductView(CreateView):
    model = Products
    template_name = 'tweak_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/tweak_product"


class CustomizeTweakProductView(CreateView):
    model = Products
    template_name = 'customize_tweak_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/customize_tweak_product"