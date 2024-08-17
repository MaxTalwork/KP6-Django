from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                           home,)

app_name = MailingConfig.name
urlpatterns = [
    path('', home, name='product_list'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
