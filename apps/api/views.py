from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import UserSerializer, CategorySerializer, ProductSerializer, ProductReviewSerializer, \
    FavoriteSerializer
from apps.shop.models import Category, Product, ProductReview, Favorite
from apps.users.models import User


# Create your views here.
class LandingPageView(APIView):
    def get(self, request):
        return Response(data={'message': 'Hello world!', "users": "http://localhost:8000/api/v1/users/",
                              "categories": "http://localhost:8000/api/v1/categories/",
                              "products": "http://localhost:8000/api/v1/products/",
                              "products/reviews": "http://localhost:8000/api/v1/product/%3Cint:pk%3E/reviews/",
                              "favourites": "http://localhost:8000/api/v1/favourites/"})

    def post(self, request):
        return Response(data={'post api': 'This is post request api'})


class UserAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filterset_fields = ('is_active', 'is_staff', 'is_superuser', 'born')
    pagination_class = LimitOffsetPagination


class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'description', 'category__name')
    filterset_fields = ('is_active', 'category__name')
    pagination_class = LimitOffsetPagination


class ProductReviewAPIViewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class FavoriteAPIViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
