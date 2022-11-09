from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from applications.order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
