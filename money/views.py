from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from .models import People
from .serializers import PeopleSerializer

class TransferAPIView(generics.CreateAPIView):
    serializer_class = PeopleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name1 = serializer.validated_data.get('fromPerson')
        name2 = serializer.validated_data.get('toPerson')
        amount = serializer.validated_data.get('transfer_amount')

        try:
            with transaction.atomic():
                name1_obj = People.objects.select_for_update().get(name=name1)
                name2_obj = People.objects.select_for_update().get(name=name2)

                
                if name1_obj.amount < amount:
                    raise ValueError('Your money is not enough')

                
                name1_obj.amount -= amount
                name1_obj.save()

                name2_obj.amount += amount
                name2_obj.save()

                return Response({'message': 'Transfer successful'})

        except People.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


