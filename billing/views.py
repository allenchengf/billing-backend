from rest_framework.generics import GenericAPIView
from .models import Customer
from .serializers import CustomerSerializer
from django.http import JsonResponse
from django.db import transaction


class CustomersView(GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **krgs):
        customers = self.get_queryset()
        serializer = self.serializer_class(customers, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)

