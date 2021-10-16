from django.urls import path
from . import views

app_name = 'capp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:slug>/', views.category_block, name='category_link'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]