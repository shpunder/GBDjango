from django.db import models
from django.conf import settings
from products.models import Product

class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)



    def basket_calculate(self, user):
        basket_calculate = {'count': 0, 'sum': 0}
        basket = Basket.objects.filter(user=user)
        for item in basket:
            basket_calculate['count'] += item.quantity
            basket_calculate['sum'] += Product.objects.get(id=item.product.id).cost * item.quantity

        return basket_calculate
