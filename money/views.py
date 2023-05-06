from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from django.db import transaction

from .models import People
from .serializers import TransferMoneySerializer, CreatePeopleSerializer


class TransferView(generics.CreateAPIView):
    serializer_class = TransferMoneySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name1 = serializer.validated_data.get('from_person')
        name2 = serializer.validated_data.get('to_person')
        transferred_money = serializer.validated_data.get('transfer_amount')

        try:
            with transaction.atomic():
                name1_obj = People.objects.select_for_update().get(name=name1)
                name2_obj = People.objects.select_for_update().get(name=name2)

                if name1_obj.amount < transferred_money:
                    raise ValueError(f"{name1}'s money is not enough")

                elif name1_obj == name2_obj:
                    raise ValueError(f"{name1} cannot transfer money to itself!")

                name1_obj.amount -= transferred_money
                name1_obj.save()

                name2_obj.amount += transferred_money
                name2_obj.save()

                return Response({
                    'message': 'Transfer successful',
                    'data': serializer.data,
                }, status=status.HTTP_200_OK)

        except People.DoesNotExist:
            return Response({'error': f"{name2} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.ListCreateAPIView):
    serializer_class = CreatePeopleSerializer
    queryset = People.objects.all().order_by('-id')


class APIRootView(APIView):
    def get(self, request):
        data = {
            'create': reverse('create', request=request),
            'transfer': reverse('transfer', request=request),
        }

        return Response(data)
