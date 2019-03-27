from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from products.models import Product


def basket_detail(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)

def basket_add(request, idx):
    product = get_object_or_404(Product, id=idx)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, idx):
    content = {}
    return render(request, 'basketapp/basket.html', content)
