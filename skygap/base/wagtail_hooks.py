from wagtail import hooks
from wagtail.admin.userbar import AccessibilityItem
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from skygap.base.models import *
from skygap.designs.models import Design
from skygap.products.models import Product


class CustomAccessibilityItem(AccessibilityItem):
    axe_run_only = None


@hooks.register("construct_wagtail_userbar")
def replace_userbar_accessibility_item(request, items):
    items[:] = [
        CustomAccessibilityItem() if isinstance(item, AccessibilityItem) else item
        for item in items
    ]


class ProductAdmin(ModelAdmin):
    model = Product
    search_fields = ("id", "name")
    inspect_view_enabled = True

    
class DesignAdmin(ModelAdmin):
    model = Design
    search_fields = ("id", "name")
    inspect_view_enabled = True



class ProductAdminGroup(ModelAdminGroup):
    menu_label = "Product | Design"
    menu_order = 200
    items = (ProductAdmin, DesignAdmin)


class LogoViewSet(SnippetViewSet):
    model = Logo


class AddressViewSet(SnippetViewSet):
    model = Address


class EmailViewSet(SnippetViewSet):
    model = Email


class PhoneViewSet(SnippetViewSet):
    model = Phone


class CopyrightViewSet(SnippetViewSet):
    model = Copyright


class BrandViewSetGroup(SnippetViewSetGroup):
    menu_label = "Brand Info"
    menu_order = 300
    items = (
        LogoViewSet,
        AddressViewSet,
        EmailViewSet,
        PhoneViewSet,
        CopyrightViewSet
    )


modeladmin_register(ProductAdminGroup)
register_snippet(BrandViewSetGroup)