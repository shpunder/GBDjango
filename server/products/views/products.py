import json
# from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from products.models import Product, ProductCategory, UploadFileForm
from products.forms import ProductForm
from basketapp.models import Basket


def product_rest_list(request):
    data = []
    object_list = Product.objects.all()
    for item in object_list:
        data.append(
            {
                'id': item.id,
                'name': item.name,
                'image': item.image.url if item.image else None,
                'category': item.category.name,
                'description': item.description,
                'cost': item.cost,
                'created': item.created,
                'modified': item.modified,
            }
        )
    return JsonResponse({'results': data})


def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES
        )
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


def product_update(request, idx):
    obj = get_object_or_404(Product, id=idx)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(
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


def product_delete(request, idx):
    obj = get_object_or_404(Product, id=idx)

    if request.method == 'POST':
        obj.delete()

        return redirect('products:main')
    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )


def product_list(request):

    basket = Basket()
    basket_calculate = None
    if request.user.is_authenticated:
        basket_calculate = basket.basket_calculate(request.user)



    return render(
        request,
        'products/index.html',
        {
            'basket_calculate': basket_calculate,
            'object_list': Product.objects.all()[:2],
            'category_list': ProductCategory.objects.all(),
        }
    )


def product_detail(request, idx):
    obj = get_object_or_404(Product, id=idx)
    return render(
        request,
        'products/detail.html',
        {
            'object': obj,
        }
    )


# загрузка из json файла
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        save_path = 'upload/' # папка для сохранения файлов
        if form.is_valid():
            # сохранение файла
            with open(save_path+request.FILES['file'].name, 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            with open(save_path+request.FILES['file'].name, 'r', encoding='utf-8') as file:
                obj = json.load(file)
                for item in obj:
                    category = ProductCategory.objects.get(id=item['category'])
                    product = Product()
                    product.name = item['name']
                    product.description = item['description']
                    product.cost = item['cost']
                    product.category = category
                    product.save()
            return render(request, "products/upload_result.html", {'object': obj})
    else:
        form = UploadFileForm()
        return render(request, "products/upload_file.html", {'form': form})
        