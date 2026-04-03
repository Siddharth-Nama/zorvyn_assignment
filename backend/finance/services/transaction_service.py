from django.shortcuts import get_object_or_404
from ..models import Transaction

class TransactionService:
    @staticmethod
    def create_transaction(user, validated_data):
        return Transaction.objects.create(created_by=user, **validated_data)

    @staticmethod
    def update_transaction(transaction_id, validated_data):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        for attr, value in validated_data.items():
            setattr(transaction, attr, value)
        transaction.save()
        return transaction

    @staticmethod
    def soft_delete_transaction(transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.is_deleted = True
        transaction.save()
        return transaction
