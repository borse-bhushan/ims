"""
Category viewset for managing Categories.
"""

from rest_framework import viewsets

from base.views.base import BaseView

from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission


from .db_access import category_manager
from .serializers import CategorySerializer, CategoryQuerySerializer


MODULE = "Category"


class CategoryViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing category.
    """

    manager = category_manager
    lookup_field = "category_id"
    serializer_class = CategorySerializer
    list_serializer_class = CategoryQuerySerializer
    search_fields = ["category_code", "category_name"]

    get_authenticators = get_authentication_classes

    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
