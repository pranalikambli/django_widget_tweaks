from django.urls import path

from . import views

urlpatterns = [
    path('basic_product/', views.BasicProductView.as_view(), name="basic_product_view"),
    path('crispy_product/', views.TweakProductView.as_view(), name="tweak_product_view"),
    path('customize_tweak_product/', views.CustomizeTweakProductView.as_view(), name="customize_tweak_product_view"),
]