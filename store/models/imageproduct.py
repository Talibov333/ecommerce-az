from django.db import models
from .product import Product
from django.utils.html import mark_safe

class ImageProduct(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=50,blank=True)
	image = models.ImageField(upload_to='upload/products')

	class Meta:
		verbose_name_plural = 'Mehsul sekil galerisi'

	def __str__ (self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" height="150" />'.format(self.image.url))
	image_tag.short_description = 'Image'




	@staticmethod
	def getAllProduct():
		return ImageProduct.objects.all()
