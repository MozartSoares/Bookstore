from rest_framework.viewsets import ModelViewset

from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(ModelViewset):
  
  serializer_class = ProductSerializer
  
  def get_queryset(self):
    return Product.objects.all()