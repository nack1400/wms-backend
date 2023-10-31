from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import (
    CustomerSerializer,
    ConsigneeSerializer,
    CarrierSerializer,
    DeliveryAddressSerializer,
    BankSerializer,
    ContactSerializer,
)


def customer_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all customers",
            operation_description="Retrieve a list of all customers.",
            responses={200: CustomerSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new customer",
            operation_description="Create a new customer with the provided data.",
            request_body=CustomerSerializer,
            responses={201: CustomerSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def customer_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a customer",
            operation_description="Retrieve details of a customer by ID.",
            responses={200: CustomerSerializer()},
        )
        def get(self, request, pk, *args, **kwargs):
            return super().get(request, pk, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a customer",
            operation_description="Update a customer with the provided data.",
            request_body=CustomerSerializer,
            responses={200: CustomerSerializer()},
        )
        def put(self, request, pk, *args, **kwargs):
            return super().put(request, pk, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a customer",
            operation_description="Delete a customer by ID.",
            responses={204: "No Content"},
        )
        def delete(self, request, pk, *args, **kwargs):
            return super().delete(request, pk, *args, **kwargs)

    return DecoratedView


def consignee_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all consignees",
            operation_description="Retrieve a list of all consignees.",
            responses={200: ConsigneeSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new consignee",
            operation_description="Create a new consignee with the provided data.",
            request_body=ConsigneeSerializer,
            responses={201: ConsigneeSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def consignee_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a consignee details",
            operation_description="Retrieve details of a specific consignee.",
            responses={200: ConsigneeSerializer()},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a consignee",
            operation_description="Update an existing consignee with the provided data.",
            request_body=ConsigneeSerializer,
            responses={200: ConsigneeSerializer()},
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a consignee",
            operation_description="Delete a specific consignee.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView


def carrier_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all carriers",
            operation_description="Retrieve a list of all carriers.",
            responses={200: CarrierSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new carrier",
            operation_description="Create a new carrier with the provided data.",
            request_body=CarrierSerializer,
            responses={201: CarrierSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def carrier_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a carrier details",
            operation_description="Retrieve details of a specific carrier.",
            responses={200: CarrierSerializer()},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a carrier",
            operation_description="Update an existing carrier with the provided data.",
            request_body=CarrierSerializer,
            responses={200: CarrierSerializer()},
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a carrier",
            operation_description="Delete a specific carrier.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView


def delivery_address_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all delivery addresses",
            operation_description="Retrieve a list of all delivery addresses.",
            responses={200: DeliveryAddressSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new delivery address",
            operation_description="Create a new delivery address with the provided data.",
            request_body=DeliveryAddressSerializer,
            responses={201: DeliveryAddressSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def delivery_address_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a delivery address details",
            operation_description="Retrieve details of a specific delivery address.",
            responses={200: DeliveryAddressSerializer()},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a delivery address",
            operation_description="Update an existing delivery address with the provided data.",
            request_body=DeliveryAddressSerializer,
            responses={200: DeliveryAddressSerializer()},
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a delivery address",
            operation_description="Delete a specific delivery address.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView


def bank_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all banks",
            operation_description="Retrieve a list of all banks.",
            responses={200: BankSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new bank",
            operation_description="Create a new bank with the provided data.",
            request_body=BankSerializer,
            responses={201: BankSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def bank_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a bank details",
            operation_description="Retrieve details of a specific bank.",
            responses={200: BankSerializer()},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a bank",
            operation_description="Update an existing bank with the provided data.",
            request_body=BankSerializer,
            responses={200: BankSerializer()},
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a bank",
            operation_description="Delete a specific bank.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView


def contact_list_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="List all contacts",
            operation_description="Retrieve a list of all contacts.",
            responses={200: ContactSerializer(many=True)},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Create a new contact",
            operation_description="Create a new contact with the provided data.",
            request_body=ContactSerializer,
            responses={201: ContactSerializer()},
        )
        def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    return DecoratedView


def contact_detail_swagger(view_class):
    class DecoratedView(view_class):
        @swagger_auto_schema(
            operation_summary="Retrieve a contact details",
            operation_description="Retrieve details of a specific contact.",
            responses={200: ContactSerializer()},
        )
        def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Update a contact",
            operation_description="Update an existing contact with the provided data.",
            request_body=ContactSerializer,
            responses={200: ContactSerializer()},
        )
        def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)

        @swagger_auto_schema(
            operation_summary="Delete a contact",
            operation_description="Delete a specific contact.",
        )
        def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)

    return DecoratedView
