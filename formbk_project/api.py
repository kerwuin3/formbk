from rest_framework import viewsets, permissions
from .models import Form
from .serializers import FormSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormSerializer