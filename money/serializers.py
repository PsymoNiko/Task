from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    fromPerson = serializers.CharField(max_length=10)
    toPerson = serializers.CharField(max_length=10)
    transfer_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = People
        fields = ["fromPerson", "toPerson", "transfer_amount"]

