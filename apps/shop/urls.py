from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ShopPageView, ProductDetailPageView, \
    ProductCreatePageView, FilterProductsPageView, CategoryPageView, SearchView

app_name = 'shop'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', AboutPageView.as_view(), name='home'),
    path('', ContactPageView.as_view(), name='home'),
    path('filter/', FilterProductsPageView.as_view(), name='filter'),
    path('shop/search/', SearchView.as_view(), name='search'),
    path('shop/category/<int:id>', CategoryPageView.as_view(), name='category'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('products/<int:pk>', ProductDetailPageView.as_view(), name='product-detail'),
    path('product-create/', ProductCreatePageView.as_view(), name='product-create'),
]