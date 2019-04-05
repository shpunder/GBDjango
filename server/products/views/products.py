import json
# from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import (
    View, CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.contrib.auth.decorators import (
    login_required, user_passes_test
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.urls import reverse_lazy
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


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'image', 'category', 'description', 'cost']
    template_name = 'categories/create.html'
    success_url = 'products:main'

    # def get(self, *args, **kwargs):
    #     return render(
    #         self.request,
    #         self.template_name,
    #         {'form': self.form_class}
    #     )

    # def post(self, *args, **kwargs):
    #     form = self.form_class(
    #         data=self.request.POST,
    #         files=self.request.FILES
    #     )
    #     if form.is_valid():
    #         form.save()
    #         return redirect(self.success_url)

    #     return render(
    #         self.request,
    #         self.template_name,
    #         {'form': form}
    #     )

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'image', 'category', 'description', 'cost']
    template_name = 'categories/update.html'
    success_url = 'products:main'


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'categories/delete.html'
    success_url = 'products:main'
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        return self.request.user.is_superuser


class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'

    def get_context_data(self, *args, **kwargs):
        obj = Product.objects.all()
        page_num = self.request.GET.get('page')
        paginator = Paginator(obj, 2)
        return {
            'object': obj,
            'page_object': paginator.get_page(page_num)
        }


class ProductDetail(DetailView):
    model = Product
    template_name = 'categories/detail.html'


def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            # тут была строка print(request.user.first_name)
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

@login_required
@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, idx):
    obj = get_object_or_404(Product, id=idx)

    if request.method == 'POST':
        obj.delete()

        return redirect('/products/')
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
        save_path = 'upload/'  # папка для сохранения файлов
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
