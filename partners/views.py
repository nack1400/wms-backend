from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *
from .swagger import *


# Customer
@customer_list_swagger
class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerWithAttachmentsSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@customer_detail_swagger
class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@customer_attachment_create_swagger
class CustomerAttachmentCreate(APIView):
    def post(self, request, customer_pk):
        try:
            customer = Customer.objects.get(pk=customer_pk)
        except Customer.DoesNotExist:
            raise NotFound("Customer not found")

        serializer = CustomerAttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["customer"] = customer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@customer_attachment_delete_swagger
class CustomerAttachmentDelete(APIView):
    def delete(self, request, customer_pk, attachment_pk):
        try:
            customer = Customer.objects.get(pk=customer_pk)
        except Customer.DoesNotExist:
            raise NotFound("Customer not found")

        try:
            attachment = CustomerAttachment.objects.get(
                pk=attachment_pk, customer=customer
            )
        except CustomerAttachment.DoesNotExist:
            raise NotFound("Attachment not found")

        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Consignee
@consignee_list_swagger
class ConsigneeList(APIView):
    def get(self, request):
        consignees = Consignee.objects.all()
        serializer = ConsigneeWithAttachmentsSerializer(consignees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsigneeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@consignee_detail_swagger
class ConsigneeDetail(APIView):
    def get_object(self, pk):
        try:
            return Consignee.objects.get(pk=pk)
        except Consignee.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        consignee = self.get_object(pk)
        serializer = ConsigneeWithAttachmentsSerializer(consignee)
        return Response(serializer.data)

    def put(self, request, pk):
        consignee = self.get_object(pk)
        serializer = ConsigneeSerializer(consignee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        consignee = self.get_object(pk)
        consignee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@consignee_attachment_create_swagger
class ConsigneeAttachmentCreate(APIView):
    def post(self, request, consignee_pk):
        try:
            consignee = Consignee.objects.get(pk=consignee_pk)
        except Consignee.DoesNotExist:
            raise NotFound("Consignee not found")

        serializer = ConsigneeAttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["consignee"] = consignee
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@consignee_attachment_delete_swagger
class ConsigneeAttachmentDelete(APIView):
    def delete(self, request, consignee_pk, attachment_pk):
        try:
            consignee = Consignee.objects.get(pk=consignee_pk)
        except Consignee.DoesNotExist:
            raise NotFound("Consignee not found")

        try:
            attachment = ConsigneeAttachment.objects.get(
                pk=attachment_pk, consignee=consignee
            )
        except ConsigneeAttachment.DoesNotExist:
            raise NotFound("Attachment not found")

        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Carrier
@carrier_list_swagger
class CarrierList(APIView):
    def get(self, request):
        carriers = Carrier.objects.all()
        serializer = CarrierWithAttachmentsSerializer(carriers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarrierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@carrier_detail_swagger
class CarrierDetail(APIView):
    def get_object(self, pk):
        try:
            return Carrier.objects.get(pk=pk)
        except Carrier.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        carrier = self.get_object(pk)
        serializer = CarrierWithAttachmentsSerializer(carrier)
        return Response(serializer.data)

    def put(self, request, pk):
        carrier = self.get_object(pk)
        serializer = CarrierSerializer(carrier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        carrier = self.get_object(pk)
        carrier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@carrier_attachment_create_swagger
class CarrierAttachmentCreate(APIView):
    def post(self, request, carrier_pk):
        try:
            carrier = Carrier.objects.get(pk=carrier_pk)
        except Carrier.DoesNotExist:
            raise NotFound("Carrier not found")

        serializer = CarrierAttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["carrier"] = carrier
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@carrier_attachment_delete_swagger
class CarrierAttachmentDelete(APIView):
    def delete(self, request, carrier_pk, attachment_pk):
        try:
            carrier = Carrier.objects.get(pk=carrier_pk)
        except Carrier.DoesNotExist:
            raise NotFound("Carrier not found")

        try:
            attachment = CarrierAttachment.objects.get(
                pk=attachment_pk, carrier=carrier
            )
        except CarrierAttachment.DoesNotExist:
            raise NotFound("Attachment not found")

        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Delivery
@delivery_address_list_swagger
class DeliveryAddressList(APIView):
    def get(self, request):
        delivery_addresses = DeliveryAddress.objects.all()
        serializer = DeliveryAddressSerializer(delivery_addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliveryAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@delivery_address_detail_swagger
class DeliveryAddressDetail(APIView):
    def get_object(self, pk):
        try:
            return DeliveryAddress.objects.get(pk=pk)
        except DeliveryAddress.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        delivery_address = self.get_object(pk)
        serializer = DeliveryAddressSerializer(delivery_address)
        return Response(serializer.data)

    def put(self, request, pk):
        delivery_address = self.get_object(pk)
        serializer = DeliveryAddressSerializer(delivery_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delivery_address = self.get_object(pk)
        delivery_address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Bank
@bank_list_swagger
class BankList(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@bank_detail_swagger
class BankDetail(APIView):
    def get_object(self, pk):
        try:
            return Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    def put(self, request, pk):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bank = self.get_object(pk)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Contact
@contact_list_swagger
class ContactList(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@contact_detail_swagger
class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
