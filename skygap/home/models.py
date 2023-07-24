from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class HomePage(Page):
    # Introduction section
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Banner image (<sizing guide>)"
    )
    introheader = models.CharField(max_length=254, default="SKYGAP")
    subheader = models.CharField(blank=True, max_length=254)
    description = RichTextField(blank=True)
    square_image_left = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Square image on homepage. (Preferably a design image)"
    )
    square_image_right = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Square image on homepage. (Preferably a design image)"
    )
    landscape_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape image on homepage. (Preferably a product image)"
    )

    # Admin panel
    content_panels = Page.content_panels + [
        FieldPanel("banner"),
        MultiFieldPanel(
            [
                FieldPanel("introheader"),
                FieldPanel("subheader"),
                FieldPanel("description"),
                MultiFieldPanel(
                    [
                        FieldPanel("square_image_left"),
                        FieldPanel("square_image_right"),
                        FieldPanel("landscape_image"),
                    ]
                )
            ],
            heading="Introduction Section"
        )
    ]


# Slideshow Images
# class SlideshowImage(Orderable):
#     page = ParentalKey(
#         HomePage,
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name='slideshow_images')
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True, 
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text="Slideshow images on homepage (<sizing>)"
#     )
#     caption = models.CharField(blank=True, max_length=254)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]


    
