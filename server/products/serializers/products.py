from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
)

from products.models import Product


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    created = SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'image', 'category', 'description', 'cost', 'created')

    def get_category(self, obj):
        if obj.category:
            return obj.category.name

    def get_created(self, obj):
        return obj.created
