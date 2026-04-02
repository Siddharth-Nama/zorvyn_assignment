from django.db import models
from django.conf import settings
from .managers import SoftDeleteManager

class TransactionType(models.TextChoices):
    INCOME = 'INCOME', 'Income'
    EXPENSE = 'EXPENSE', 'Expense'

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SoftDeleteManager()

    class Meta:
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['created_by', 'is_deleted']),
        ]

    def delete(self, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, **kwargs):
        super().delete(**kwargs)

    def __str__(self):
        return f"{self.type} - {self.amount} ({self.date})"
