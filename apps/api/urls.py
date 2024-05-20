from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api import views
from apps.api.views import LandingPageView

router = DefaultRouter()
router.register('users', views.UserAPIViewSet)
router.register('categories', views.CategoryAPIViewSet)
router.register('products', views.ProductAPIViewSet)
router.register('product/<int:pk>/reviews', views.ProductReviewAPIViewSet)
router.register('favourites', views.FavoriteAPIViewSet)

app_name = 'api'
urlpatterns = [
    path('landing/', LandingPageView.as_view(), name='landing'),
    path('', include(router.urls)),
]