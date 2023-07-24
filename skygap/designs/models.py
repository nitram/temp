from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel
from wagtail.models import (
    DraftStateMixin,
    Orderable,
    Page,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet


# PAGES
class DesignPage(Page):
    pass


# SNIPPETS
@register_snippet
class Design(DraftStateMixin, RevisionMixin, ClusterableModel):
    id = models.AutoField(
        primary_key=True,
        unique=True,
    )
    name = models.CharField(
        max_length=254,
        verbose_name="Design Name",
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Product type icon (<sizing guide>)"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
        # InlinePanel("design_images", label="Design Images"),
    ]

    def __str__(self):
        return f"{self.name}"


# Product Images
# class DesignImage(Orderable):
#     parent = ParentalKey(
#         Design,
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name='design_images')
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True, 
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text="Design images; first image will be thumbnail (square)"
#     )

#     panels = [
#         FieldPanel('image'),
#     ]