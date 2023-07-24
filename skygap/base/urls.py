from django.urls import path

from . import views

urlpatterns = [
    path('gtprods/<int:start>/<int:end>/<int:page_id>', views.load_products, name="load_products"),
    path('gtdes/<int:start>/<int:end>', views.load_designs, name="load_design"),
    path('gtprodimgs/<int:product_id>', views.load_product_images, name="load_product_images"),
    path('gtimg/<int:image_id>', views.load_image, name="load_image"),
]