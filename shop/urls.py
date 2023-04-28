from django.urls import path
from shopping.controller import add_product, home, delete_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('add/', add_product, name='add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
