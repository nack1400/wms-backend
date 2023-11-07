from django.urls import path
from . import views

urlpatterns = [
    path("customers", views.CustomerList.as_view(), name="customer-list"),
    path("customers/<int:pk>", views.CustomerDetail.as_view(), name="customer-detail"),
    path(
        "customers/<int:customer_pk>/attachments",
        views.CustomerAttachmentCreate.as_view(),
        name="customer-attachment-create",
    ),
    path(
        "customers/<int:customer_pk>/attachments/<int:attachment_pk>",
        views.CustomerAttachmentDelete.as_view(),
        name="customer-attachment-delete",
    ),
    path("consignees", views.ConsigneeList.as_view(), name="consignee-list"),
    path(
        "consignees/<int:pk>", views.ConsigneeDetail.as_view(), name="consignee-detail"
    ),
    path(
        "consignees/<int:consignee_pk>/attachments",
        views.ConsigneeAttachmentCreate.as_view(),
        name="consignee-attachment-create",
    ),
    path(
        "consignees/<int:consignee_pk>/attachments/<int:attachment_pk>",
        views.ConsigneeAttachmentDelete.as_view(),
        name="consignee-attachment-delete",
    ),
    path("carriers", views.CarrierList.as_view(), name="carrier-list"),
    path("carriers/<int:pk>", views.CarrierDetail.as_view(), name="carrier-detail"),
    path(
        "delivery-addresses",
        views.DeliveryAddressList.as_view(),
        name="delivery-address-list",
    ),
    path(
        "delivery-addresses/<int:pk>",
        views.DeliveryAddressDetail.as_view(),
        name="delivery-address-detail",
    ),
    path("banks", views.BankList.as_view(), name="bank-list"),
    path("banks/<int:pk>", views.BankDetail.as_view(), name="bank-detail"),
    path("contacts", views.ContactList.as_view(), name="contact-list"),
    path("contacts/<int:pk>", views.ContactDetail.as_view(), name="contact-detail"),
]
