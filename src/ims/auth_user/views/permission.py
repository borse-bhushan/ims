"""
Permission ViewSet for handling permission endpoints.
"""

from rest_framework import status, viewsets
from drf_spectacular.utils import extend_schema

from base.views import CreateView, ListView
from authentication import (
    get_authentication_classes,
    register_permission,
    get_default_authentication_class,
)

from utils.messages import success
from utils.response import generate_response
from utils.swagger import (
    responses_404,
    responses_401,
    responses_404_example,
    responses_401_example,
)

from auth_user.constants import MethodEnum
from auth_user.db_access import permission_manager
from auth_user.utils.permission import load_permission
from auth_user.serializers import PermissionListQuerySerializer
from auth_user.swagger import (
    PermissionListResponseSerializer,
    permission_list_success_example,
)

MODULE = "Permission"


class PermissionListView:
    """
    Base Permission List view
    """

    is_pagination: bool = False
    manager = permission_manager

    @extend_schema(
        responses={
            200: PermissionListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            permission_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        """Get the list of permissions and modules"""
        # pylint:disable=no-member
        return super().list_all(request, *args, **kwargs)


class ListCreatePermissionViewSet(
    PermissionListView,
    ListView,
    CreateView,
    viewsets.ViewSet,
):
    """
    Load the permission array against the tenant.
    """

    many = True
    manager = permission_manager
    is_common_data_needed = False
    serializer_class = PermissionListQuerySerializer
    list_serializer_class = PermissionListQuerySerializer
    get_authenticators = get_default_authentication_class

    @classmethod
    def get_method_view_mapping(cls):
        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }

    def save(self, data, **kwargs):
        load_permission.load_module_and_actions_for_tenants(
            request=kwargs["request"],
            tenant_id_or_list=[tenant_data["tenant_id"] for tenant_data in data],
        )
        return None

    @register_permission(
        MODULE, MethodEnum.POST, f"Create {MODULE}", create_permission=False
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PermissionViewSet(PermissionListView, ListView, viewsets.ViewSet):
    """
    ViewSet for handling permission endpoints.
    """

    get_authenticators = get_authentication_classes
