from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        if not value.isdigit():
            raise serializers.ValidationError("O CPF deve conter apenas números.")
        return value
    
    def validate(self, data):
        if data['altura'] <= 0:
            raise serializers.ValidationError("A altura deve ser um valor positivo.")
        if data['peso'] <= 0:
            raise serializers.ValidationError("O peso deve ser um valor positivo.")
        return data