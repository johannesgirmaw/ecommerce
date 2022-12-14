
from django.urls import path
from .views import ProductList, ProductDetail
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("product/<int:pk>/", ProductDetail.as_view(),
         name="product_detail"),
    path("product/", ProductList.as_view(), name="product_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
