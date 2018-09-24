from django.shortcuts import render


def catalog_list(request):

    return render(request, 'mainapp/catalog.html')


def main_page(request):

    return render(request, 'mainapp/index.html')


def product_detail(request):

    return render(request, 'mainapp/brooch.html')


def contacts(request):

    return render(request, 'mainapp/contacts.html')
