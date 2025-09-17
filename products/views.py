from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product , File , Category
from .serializers import ProductSerializer , FileSerializer , CategorySerializer


class ProductListView(APIView):
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True , context={'request': request})
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self , request , pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"} , status=404)
        seializer = ProductSerializer(product , context={'request': request})
        return Response(seializer.data)
    
class CategoryListView(APIView):
    def get(self , request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many=True , context={'request': request})
        return Response(serializer.data)
    
class CategoryDetailView(APIView):
    def get(self , request , pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"} , status=404)
        seializer = CategorySerializer(category , context={'request': request})
        return Response(seializer.data)
    
class FileListView(APIView):
    def get(self , request , product_pk):
        files = File.objects.filter(product=product_pk)
        serializer = FileSerializer(files , many=True, context={'request': request})
        return Response(serializer.data)
    
class FileDetailView(APIView):
    def get(self , request , pk , product_pk):
        try:
            f = File.objects.get(id=pk , product=product_pk)
        except File.DoesNotExist:
            return Response({"error": "File not found"} , status=404)
        serializer = FileSerializer(f , context={'request': request})
        return Response(serializer.data)