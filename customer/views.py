from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Customer, User
from .customer_serializer import CustomerSerializer
from django.http import HttpResponse


class CustomerViewSet(viewsets.ModelViewSet):
    """Customer view set class"""

    serializer_class = CustomerSerializer

    def get_queryset(self):
        """Get all the customer list"""

        customer = Customer.objects.all()
        return customer

    def create(self, request, *args, **kwargs):
        """Insert new customer"""

        customer_data = request.data

        try:
            new_user = User.objects.create(
                first_name=customer_data["user"]["first_name"],
                last_name=customer_data["user"]["last_name"],
                email=customer_data["user"]["email"],
                phone_number=customer_data["user"]["phone_number"])

            new_user.save()

            new_customer = Customer.objects.create(
                profile_number=customer_data["profile_number"], user=new_user)
            new_customer.save()

            serializer = CustomerSerializer(new_customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return HttpResponse(content="Invalid user data", status=status.HTTP_400_BAD_REQUEST)
