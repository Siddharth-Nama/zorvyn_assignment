from rest_framework import viewset, permissions, status
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .services.transaction_service import TransactionService
from accounts.permissions import IsAdmin, IsAnalyst, IsViewer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        TransactionService.create_transaction(self.request.user, serializer.validated_data)

    def perform_update(self, serializer):
        TransactionService.update_transaction(self.get_object().id, serializer.validated_data)

    def perform_destroy(self, instance):
        TransactionService.soft_delete_transaction(instance.id)
