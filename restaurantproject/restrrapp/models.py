# from django.db import models
#
#
# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=290, unique=True)
#     desc = models.TextField(blank=True)
#     img = models.ImageField(upload_to='category', blank=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return   '{}'.format(self.name)
#
#
# class Items1(models.Model):
#     name = models.CharField(max_length=220, unique=True)
#     slug = models.SlugField(max_length=290, unique=True)
#     desc = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='items1', blank=True)
#     avialable = models.BooleanField(default=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'items1'
#         verbose_name_plural = 'items1'
#
#     def __str__(self):
#         return   '{}'.format(self.name)
