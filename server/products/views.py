import json
from django.shortcuts import render, redirect
from .models import Product, ProductCategory, UploadFileForm
from .forms import ProductCategoryForm, ProductCategoryModelForm


def product_list(request):
    return render(
        request,
        'products/index.html',
        {
            'object_list': Product.objects.all(),
            'category_list': ProductCategory.objects.all()
        }
    )


def product_detail(request, idx):
    return render(
        request,
        'products/detail.html',
        {'object': Product.objects.get(id=idx)}
    )


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
    return render(
        request,
        'products/category-detail.html',
        {
            'object': ProductCategory.objects.get(id=idx),
            'product_list': Product.objects.filter(category=ProductCategory.objects.get(id=idx))
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


# 6. Реализовать автоматическое формирование меню категорий по данным из модели.
# 7. *Создать диспетчер URL в приложении. Скорректировать динамические URL-адреса в шаблонах.
# Поработать с имитацией переходов по категориям в адресной строке браузера.
# 8. *Организовать загрузку данных в базу из файла.
