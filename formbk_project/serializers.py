from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'user', 'email', 'password', 'created_at')
        read_only_fields = ('created_at', )