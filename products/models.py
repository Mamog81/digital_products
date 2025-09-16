from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description") , blank=True )


class Product(models.Model):
    pass


class File(models.Model):
    pass