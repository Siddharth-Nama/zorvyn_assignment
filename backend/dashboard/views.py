from rest_framework.views import APIView
from rest_framework.response import Response
from .services import DashboardService
from accounts.permissions import IsAnalyst, IsAdmin

class DashboardSummaryView(APIView):
    permission_classes = [IsAnalyst | IsAdmin]

    def get(self, request):
        stats = DashboardService.get_summary_stats(request.user)
        breakdown = DashboardService.get_category_breakdown(request.user)
        
        return Response({
            'summary': stats,
            'category_breakdown': breakdown
        })
