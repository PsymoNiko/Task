from rest_framework import serializers
from .models import People

import re

from typing import Union


class TransferMoneySerializer(serializers.ModelSerializer):
    from_person = serializers.PrimaryKeyRelatedField(queryset=People.objects.all())
    to_person = serializers.CharField(max_length=10)
    transfer_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = People
        fields = ["from_person", "to_person", "transfer_amount"]

    def validate_to_person(self, obj: str) -> str:
        if len(obj) > 10:
            raise serializers.ValidationError()
        return obj

    def validate_transfer_amount(self, value: Union[int, float]) -> float:
        if re.match('[a-zA-Z]', str(value)):
            raise serializers.ValidationError('Your amount of money must be number')
        return value


class CreatePeopleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    class Meta:
        model = People
        exclude = ('is_deleted', 'created_at', 'modified_at',)

    def create(self, validated_data):
        if People.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('This name is already exists')
        return People.objects.create(**validated_data)

    def validate_name(self, obj: str) -> str:
        if len(obj) > 10:
            raise serializers.ValidationError()
        return obj

    def validate_amount(self, value: Union[int, float]) -> float:
        if re.match('[a-zA-Z]', str(value)):
            raise serializers.ValidationError('Your amount of money must be number')
        elif len(str(value)) > 10:
            raise serializers.ValidationError('Amount of money must contain maximum 10 digits')
        return value
