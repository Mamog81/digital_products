from rest_framework import serializers
from .models import Product, Category , File

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title' , 'avatar' , 'url']
        
class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ['id', 'product', 'title', 'file' , 'file_type']
    def get_file_type (self , obj):
        return obj.get_file_type_display()
        
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True, source='file_set')
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'avatar', 'categories' , 'files' , 'url']

