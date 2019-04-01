from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from basketapp.models import Basket
from products.models import Product


@login_required
def basket_detail(request):
    page_title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user)
    basket = Basket()
    basket_calculate = basket.basket_calculate(request.user)

    content = {
        'basket_calculate': basket_calculate,
        'page_title': page_title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, idx):
    product = get_object_or_404(Product, id=idx)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, idx):
    basket_record = get_object_or_404(Basket, id=idx)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
