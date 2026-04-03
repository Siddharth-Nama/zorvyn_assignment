from django.db.models import Sum
from finance.models import Transaction, TransactionType

class DashboardService:
    @staticmethod
    def get_summary_stats(user):
        transactions = Transaction.objects.filter(created_by=user)
        
        income = transactions.filter(type=TransactionType.INCOME).aggregate(total=Sum('amount'))['total'] or 0
        expense = transactions.filter(type=TransactionType.EXPENSE).aggregate(total=Sum('amount'))['total'] or 0
        
        return {
            'total_income': income,
            'total_expense': expense,
            'net_balance': income - expense
        }

    @staticmethod
    def get_category_breakdown(user):
        transactions = Transaction.objects.filter(created_by=user)
        return transactions.values('category').annotate(total=Sum('amount')).order_by('-total')
