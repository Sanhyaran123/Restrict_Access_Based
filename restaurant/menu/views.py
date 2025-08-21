from rest_framework import viewsets, permissions
from .models import Menu
from .serializers import MenuSerializer
from core.permissions import IsAdminOrManager

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  # anyone can view
        return [permissions.IsAuthenticated(), IsAdminOrManager()]  # restricted