from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication #autenticação de sessão e autenticação básica
from rest_framework.permissions import IsAuthenticated #intercepta chamadas no middleware para ver se o usuário está autenticado
from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
  #professor muito louco botou autenticação no product ????? kkkkkkkkkkk
  authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
  permission_classes = [IsAuthenticated]
  serializer_class = ProductSerializer
  
  def get_queryset(self):
    return Product.objects.all().order_by('id') 