from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer-list"),
    path("customers/<int:pk>/", views.CustomerDetail.as_view(), name="customer-detail"),
    path("consignees/", views.ConsigneeList.as_view(), name="consignee-list"),  # 추가
    path(
        "consignees/<int:pk>/", views.ConsigneeDetail.as_view(), name="consignee-detail"
    ),
]
