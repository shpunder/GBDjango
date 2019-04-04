from django.contrib import admin
from .models import Product, ProductCategory
from django.template.loader import render_to_string


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'description', 'cost']
    
    list_filter = [
        'category', 'modified', 'created'
    ]

    search_fields = [
        'name', 'description'
    ]

    fieldsets = (
        (
            None , {
                'fields': ('name', 'category')
            }
        ),
        (
            'All', {
                'fields': ('image', 'description', 'cost')
            }
        ),
    )


    def picture(self, obj):
        return render_to_string (
            'products/components/picture.html',
            {'image': obj.image}
        )


class ProductInline(admin.TabularInline):
    model = Product
    

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'products_num']

    list_filter = [
        'name'
    ]

    inlines = [
        ProductInline
    ]

    search_fields = [
        'name'
    ]

    def products_num (self, obj):
        return obj.product_set.count()

