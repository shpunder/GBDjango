from django.shortcuts import render
import datetime
import json


def main(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html', {'current_date': datetime.datetime.now()})


def contacts(request):
    with open('data.json', 'r', encoding='utf-8') as file:
        contacts = json.load(file)
    return render(
        request,
        'mainapp/contacts.html',
        {'contacts': contacts}
    )
