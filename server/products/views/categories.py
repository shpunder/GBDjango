from django.shortcuts import (
    render, redirect, get_object_or_404
)

from products.models import ProductCategory, Product
from products.forms import ProductCategoryModelForm



def category_create(request):
    form = ProductCategoryModelForm()
    if request.method == 'POST':
        form = ProductCategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            # ProductCategory.objects.create(
            #     name=form.cleaned_data.get('name')
            # )
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def category_detail(request, idx):
    obj = get_object_or_404(ProductCategory, id=idx)
    return render(
        request,
        'categories/detail.html',
        {
            'object': obj,
            'category_list': ProductCategory.objects.all(),
            'product_list': Product.objects.filter(category=ProductCategory.objects.get(id=idx))
        }
    )


def category_update(request, idx):
    obj = get_object_or_404(ProductCategory, id=idx)
    form = ProductCategoryModelForm(instance=obj)
    if request.method == 'POST':
        form = ProductCategoryModelForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()

            return redirect('products:main')
    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


def category_delete(request, idx):
    obj = get_object_or_404(ProductCategory, id=idx)

    if request.method == 'POST':
        obj.delete()

        return redirect('products:main')
    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )


def category_list(request):
    return render(
        request,
        'categories/index.html',
        {'object_list': ProductCategory.objects.all()}
    )
