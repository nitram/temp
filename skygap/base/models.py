from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import (
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet


@register_snippet
class Logo(DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    name = models.CharField(blank=True, max_length=254)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Logo image (<sizing>)"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.name


# @register_snippet
# class Link(DraftStateMixin, RevisionMixin, models.Model):
#     name = models.CharField(max_length=254)
#     link = StreamField(
#         [
#             ("internal", blocks.PageChooserBlock(
#                 required=False
#             )),
#             ("external", blocks.URLBlock(
#                 required=False
#             ))
#         ],
#         blank=False,
#         max_num=1,
#         use_json_field=True
#     )
#     cta = models.BooleanField(
#         default=False,
#         verbose_name="Call to action"
#     )

#     panels = [
#         FieldPanel("name"),
#         FieldPanel("link"),
#         FieldPanel("cta"),
#     ]

#     def __str__(self):
#         return self.name


@register_snippet
class Address(DraftStateMixin, RevisionMixin, models.Model):
    street1 = models.CharField(max_length=254)
    street2 = models.CharField(blank=True, max_length=254)
    name = models.CharField(blank=True, null=True, max_length=254)
    apartment = models.CharField(blank=True, max_length=254, verbose_name="Apartment / Building")
    country = models.CharField(max_length=254, null=True)
    city = models.CharField(max_length=254, null=True)
    zipcode = models.CharField(max_length=5)

    panels = [
        FieldPanel("street1"),
        FieldPanel("street2"),
        FieldPanel("name"),
        FieldPanel("apartment"),
        FieldPanel("city"),
        FieldPanel("country"),
        FieldPanel("zipcode"),
    ]

    def __str__(self):
        return f"{self.street1}, {self.city}"
    

@register_snippet
class Email(DraftStateMixin, RevisionMixin, models.Model):
    email = models.EmailField()

    panels = [
        FieldPanel("email")
    ]

    def __str__(self):
        return self.email
    

@register_snippet
class Phone(DraftStateMixin, RevisionMixin, models.Model):
    phone = PhoneNumberField(region="US")

    panels = [
        FieldPanel("phone")
    ]

    def __str__(self):
        return self.phone.as_national
    

@register_snippet
class Copyright(DraftStateMixin, RevisionMixin, models.Model):
    text = models.TextField()

    panels = [
        FieldPanel("text")
    ]

    def __str__(self):
        return self.text
    
