from django.urls import path, include

urlpatterns = [
    path('', include("applications.category.urls")),
    path('', include("applications.product.urls")),
    path('', include("applications.order.urls"))
]
