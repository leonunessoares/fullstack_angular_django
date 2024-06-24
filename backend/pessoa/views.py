from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer
from .services import PessoaService
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def create(self, request, *args, **kwargs):
        service = PessoaService()
        return service.create_pessoa(request.data)

    def update(self, request, *args, **kwargs):
        service = PessoaService()
        return service.update_pessoa(kwargs.get('pk'), request.data)

    def destroy(self, request, *args, **kwargs):
        service = PessoaService()
        return service.delete_pessoa(kwargs.get('pk'))

    def retrieve(self, request, *args, **kwargs):
        service = PessoaService()
        return service.get_pessoa(kwargs.get('pk'))

    def list(self, request, *args, **kwargs):
        service = PessoaService()
        return service.get_all_pessoas()
    
    
@api_view(['POST'])
def calcular_peso_ideal(request):
    altura = request.data.get('altura')
    sexo = request.data.get('sexo')
    if altura is None or sexo is None:
        return Response({'error': 'Altura e sexo são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
    
    service = PessoaService()
    peso_ideal = service.calcular_peso_ideal(float(altura), sexo)
    return Response({'peso_ideal': peso_ideal}, status=status.HTTP_200_OK)