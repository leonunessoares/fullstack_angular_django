from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet,calcular_peso_ideal

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calcular_peso_ideal/', calcular_peso_ideal, name='calcular_peso_ideal'),
]
