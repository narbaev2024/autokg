from django.urls import path
from .views import CarViewSet, CarMakeViewSet, CategoryViewSet

urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car_detail'),
    path('', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),
    path('', CarMakeViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_make_list'),
    path('<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='carmake_detail'),

]
