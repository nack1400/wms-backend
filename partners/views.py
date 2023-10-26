from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Customer, Consignee, Carrier, DeliveryAddress, Contact, Bank
from .serializers import (
    CustomerSerializer,
    ConsigneeSerializer,
    CarrierSerializer,
    DeliveryAddressSerializer,
    BankSerializer,
    ContactSerializer,
)


class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ConsigneeList(APIView):
    def get(self, request):
        consignees = Consignee.objects.all()
        serializer = ConsigneeSerializer(consignees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsigneeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsigneeDetail(APIView):
    def get_object(self, pk):
        try:
            return Consignee.objects.get(pk=pk)
        except Consignee.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        consignee = self.get_object(pk)
        serializer = ConsigneeSerializer(consignee)
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


class CarrierList(APIView):
    def get(self, request):
        carriers = Carrier.objects.all()
        serializer = CarrierSerializer(carriers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarrierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarrierDetail(APIView):
    def get_object(self, pk):
        try:
            return Carrier.objects.get(pk=pk)
        except Carrier.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        carrier = self.get_object(pk)
        serializer = CarrierSerializer(carrier)
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
