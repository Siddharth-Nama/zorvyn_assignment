from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id', 'amount', 'type', 'category', 'date', 
            'description', 'created_by', 'is_deleted', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'is_deleted', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
        
    # We will override the delete behavior in the service layer
