from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


# Color model for Category
class Color(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name="Цвет")
    code = models.CharField(null=True, max_length=50, blank=True)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}"> Color</p>'.format(self.code))
        else:
            return ""
        

# Category model
class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=255, null=True, verbose_name="Название")
    image = models.ImageField(null=True, verbose_name="Фото", blank=True, default=None, upload_to='icons')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, verbose_name="Цвет", blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="{}" style="object-fit:contain; padding:4px; width: 64px; height: 64px;'
                           ' border-radius: 50%; background-color: white;"/>'.format(self.image.url))

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


# Brand model
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Бренд")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name


# Currency model
class Currency(models.Model):
    name = models.CharField(max_length=150, verbose_name="Валютная единица")

    class Meta:
        verbose_name = "Валютная единица"
        verbose_name_plural = "Валютная единицы"

    def __str__(self):
        return self.name
    

# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категории")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Бренд")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валютная единица", default=1)
    name = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextUploadingField(verbose_name="Описание")
    image = models.ImageField(upload_to="products", null=True, verbose_name="Главная фото")
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="{}" style="width:120px; height:120px"/>'.format(self.image.url))


# Image Model For Products
class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Фото")
    image = models.ImageField(upload_to="products", null=True, blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продукты"

    def __str__(self):
        return "%s" % self.product.name

    def image_tag(self):
        return format_html('<img src="{}" style="width:90px; height:90px"/>'.format(self.image.url))


# Variant model
class Variant(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255, verbose_name="Названия варианта")

    class Meta:
        verbose_name = "Названия варианта"
        verbose_name_plural = "Варианты название"


    def __str__(self):
        return self.name
    

# Variant value model
class VariantValue(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Варианты")
    value = models.CharField(max_length=255, verbose_name="Значение варианты")


    class Meta:
        verbose_name = "Значение варианты"
        verbose_name_plural = "Значение варианты"

    def __str__(self):
        return self.value
    

# Product Option Model
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, null=True,
                                verbose_name="Продукт")
    variant_name = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Варианты")
    variant_value = models.ForeignKey(VariantValue, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Значение варианты")
    price = models.FloatField(default=None, verbose_name="Цена", null=True, blank=False)
    

    class Meta:
        verbose_name = "Вариант продукта"
        verbose_name_plural = "Варианты продукты"

    def __str__(self):
        return self.product.name
    

class VariantCombination(models.Model):
    product = models.ForeignKey(Product, related_name='variant', on_delete=models.CASCADE, null=True,
                                verbose_name="Продукт")
    variant_name = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Варианты")
    variant_value = models.ForeignKey(VariantValue, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Значение варианты")
    price = models.FloatField(default=None, verbose_name="Цена", null=True, blank=False)


    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

    def __str__(self):
        return self.product.name