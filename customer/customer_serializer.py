from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """ Customer Serializer data """
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1
