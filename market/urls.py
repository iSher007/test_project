from django.urls import path, include
from .views import *


urlpatterns = [
    path('<int:shop_id>/categories/<int:category_id>/', index, name='index'),
    path('<int:shop_id>/categories/<int:category_id>/<int:product_id>/', product_detail, name='detail'),
]
