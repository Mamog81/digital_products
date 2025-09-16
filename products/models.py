from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parrent = models.ForeignKey('self', verbose_name=_("parrent"), on_delete=models.CASCADE , blank=True , null=True)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description") , blank=True ) 
    avatar = models.ImageField(_("avatar"), upload_to='categories')
    is_enable = models.BooleanField(_("is enable") , default=True  )
    created_time = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated at"), auto_now=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    
class Product(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description") , blank=True ) 
    avatar = models.ImageField(_("avatar"), upload_to='categories')
    is_enable = models.BooleanField(_("is enable") , default=True  )
    categories = models.ManyToManyField("Category", verbose_name=_("categories") , blank=True)
    created_time = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated at"), auto_now=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    




class File(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("product"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    models.FileField(_("file"), upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_("is enable") , default=True  )
    created_time = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated at"), auto_now=True)
    
        
    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        
    