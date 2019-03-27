import json
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Product, ProductCategory, UploadFileForm
from basketapp.models import Basket



def product_list(request):
    basket = Basket()
    if request.user.is_authenticated:
        basket_calculate = basket.basket_calculate(request.user)



    return render(
        request,
        'products/index.html',
        {
            'basket_calculate': basket_calculate,
            'object_list': Product.objects.all(),
            'category_list': ProductCategory.objects.all(),
        }
    )


def product_detail(request, idx):
    return render(
        request,
        'products/detail.html',
        {
            'object': Product.objects.get(id=idx),
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
        