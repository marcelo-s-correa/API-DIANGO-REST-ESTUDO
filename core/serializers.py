from rest_framework import serializers
from .models import cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('id','nome', 'endereco', 'idade')
        