from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("O campo CPF deve possuir 11 números.")      
        return value
    
    def validate_nome(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("Campo nome deve possuir ao menos 3 caracteres.")    
        return value
    
    def validate(self, data):       
        
        if data['altura'] <= 0:
            raise serializers.ValidationError("O campo altura deve ser positivo.")

        if data['peso'] <= 0:
            raise serializers.ValidationError("O campo peso deve ser positivo.")       
        return data