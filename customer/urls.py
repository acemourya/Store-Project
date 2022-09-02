from django.urls import path, include
from .views import CustomerViewSet
from rest_framework.routers import DefaultRouter

# Define router urls
router = DefaultRouter()
router.register("", CustomerViewSet, basename="customer")

# Define urls path
urlpatterns = [
    path("customer/", include(router.urls))
]
