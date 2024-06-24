from rest_framework.response import Response
from rest_framework import status
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaService:

    def create_pessoa(self, data):
        task = PessoaTask()
        return task.create(data)

    def update_pessoa(self, pk, data):
        task = PessoaTask()
        return task.update(pk, data)

    def delete_pessoa(self, pk):
        task = PessoaTask()
        return task.delete(pk)

    def get_pessoa(self, pk):
        task = PessoaTask()
        return task.get(pk)

    def get_all_pessoas(self):
        task = PessoaTask()
        return task.get_all()   
    
class PessoaTask:

    def create(self, data):
        serializer = PessoaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, pk, data):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PessoaSerializer(pessoa, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, pk):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    def get_all(self):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)
    
class Peso:

    def calcular_peso_ideal(self, altura, sexo):
        if sexo == 'M':
            peso_ideal = (72.7 * altura) - 58
        else:
            peso_ideal = (62.1 * altura) - 44.7
        return peso_ideal