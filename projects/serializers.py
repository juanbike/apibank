from rest_framework import serializers
from .models import cuentaContable

class cuentaContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuentaContable
        fields = ['cuentaContable', 'agencia', 'moneda', 'fechaHasta']