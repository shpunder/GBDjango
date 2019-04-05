from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm



def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {'title': title, 'login_form': login_form}
    return render(request, ' ', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('/auth/login')
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request):
    return HttpResponseRedirect('/')
