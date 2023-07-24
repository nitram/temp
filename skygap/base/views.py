import json

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.http import JsonResponse

from wagtail.images.models import Image

from skygap.designs.models import Design
from skygap.products.models import Product, ProductImage


# View of url: gtprods/
def load_products(request, start, end, page_id):
    if page_id == 999:
        products_data = Product.objects.filter(live=True)[start:end].values(
            'id',
            'name',
            'type',
            'primary_thumbnail',
            'secondary_thumbnail',
            'price')
    else:
        products_data = Product.objects.filter(live=True, type=page_id)[start:end].values(
            'id',
            'name',
            'type',
            'primary_thumbnail',
            'secondary_thumbnail',
            'price')

    return JsonResponse(list(products_data), safe=False)


def load_designs(request, start, end):
    designs_data = Design.objects.filter(live=True).order_by(F('id').desc())[start:end].values(
        'id',
        'name',
        'image',
    )

    return JsonResponse(list(designs_data), safe=False)


# View of url: gtprodimgs/
def load_product_images(request, product_id):
    images_data = ProductImage.objects.filter(parent=product_id).values('image')

    images_jsondata = []
    for image in images_data:
        img_id = image['image']
        images_jsondata.append(get_image(img_id))

    return JsonResponse(list(images_jsondata), safe=False)


# View of url: gtimg/
def load_image(request, image_id):
    return JsonResponse(get_image(image_id), safe=False)


# Return image data of certain image id
def get_image(image_id):
    image_data = dict(Image.objects.filter(id=image_id).values(
            'title',
            'file',
            'width',
            'height')[0])
    
    return image_data