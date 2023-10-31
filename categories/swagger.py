from rest_framework import status
from .serializers import CategoryListSerializer, CategoryDetailSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def category_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            responses={status.HTTP_200_OK: CategoryListSerializer(many=True)},
            operation_summary="Get a list of categories",
            operation_description="Retrieve a list of all categories.",
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "name": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Category name",
                        example="Example Category",
                    ),
                    "key": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Category key",
                        example="example_key",
                    ),
                    "billing_unit": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Billing unit for the category",
                        example="pallet",
                        enum=["pallet", "box", "weight", "manual"],
                    ),
                },
                required=["name", "key"],
            ),
            responses={status.HTTP_201_CREATED: CategoryListSerializer()},
            operation_summary="Create a new category",
            operation_description="Create a new category with the specified data.",
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def category_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            responses={status.HTTP_200_OK: CategoryDetailSerializer()},
            operation_summary="Get category details",
            operation_description="Retrieve details of a specific category by ID.",
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "name": openapi.Schema(
                        type=openapi.TYPE_STRING, description="Category name"
                    ),
                    "billing_unit": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Billing unit for the category",
                        example="pallet",
                        enum=["pallet", "box", "weight", "manual"],
                    ),
                },
            ),
            responses={status.HTTP_200_OK: CategoryDetailSerializer()},
            operation_summary="Update category details",
            operation_description="Update details of a specific category by ID.",
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            responses={status.HTTP_204_NO_CONTENT: "Category deleted successfully."},
            operation_summary="Delete a category",
            operation_description="Delete a specific category by ID.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView
