from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('nombre', 'descripcion','tipo','serial','valor_compra','estado_actual','persona_asignada','fecha_compra')