from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from .serializers import DashboardSerializer

# RBAC Example View
class AdminOnlyView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "message": "Only ADMIN can see this"
        })

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "tenant": request.tenant.name,
            "user": request.user.username,
            "role": request.user.role,
        }

        serializer = DashboardSerializer(data)
        return Response(serializer.data)