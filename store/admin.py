from django.contrib import admin
from .models import Product
from .models import Category
from .models import ImageProduct
from .models import Customer
from .models import Order
from .models import HomePageSetting

class ProductImageInline(admin.TabularInline):
	model = ImageProduct
	extra = 5

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date','image_tag']
	readonly_fields = ('image_tag',)
	list_display_links = ['name','category']
	list_filter = ['name', 'date']
	inlines = [ProductImageInline]
	search_fields = ['name','price']


class AdminImageProduct(admin.ModelAdmin):
	list_display = ['title','image_tag','product']
	readonly_fields = ('image_tag',)

	list_filter = ['title']




class AdminCategory(admin.ModelAdmin):
	list_display = ['name']

class AdminOrder(admin.ModelAdmin):
	list_display = ['product','customer','price','date','address','phone','completed']
	list_display_links = ['product']

class AdminCustomer(admin.ModelAdmin):
	list_display = ['name','']

admin.site.register(Product,AdminProduct)

admin.site.register(Category,AdminCategory)

admin.site.register(Customer)
admin.site.register(HomePageSetting)
admin.site.register(ImageProduct,AdminImageProduct)
admin.site.register(Order,AdminOrder)
