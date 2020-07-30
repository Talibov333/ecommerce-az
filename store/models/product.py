from django.db import models
from .category import Category
from django.utils.html import mark_safe

class Product(models.Model):
	name = models.CharField(max_length=220)
	price = models.IntegerField(default=0)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
	description = models.TextField()
	image = models.ImageField(upload_to='upload/products')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'mehsullar'

	def image_tag(self):
		return mark_safe('<img src="{}" height="120" />'.format(self.image.url))
	image_tag.short_description = 'Image'


	# All Product get
	@staticmethod
	def getAllProduct():
		return Product.objects.all()

	# Filter Product By Category
	@staticmethod
	def getProductByFilter(category_id):
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.getAllProduct()

	@staticmethod
	def getProductById(productList):
		return Product.objects.filter(id__in=productList)
