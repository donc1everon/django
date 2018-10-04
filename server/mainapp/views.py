from django.shortcuts import render, get_list_or_404, get_object_or_404

from . import models

links_menu = [
    {'href': 'main_page', 'name': 'главная'},
    {'href': 'catalog', 'name': 'каталог'},
    {'href': 'contacts', 'name': 'контакты'},
]


def main_page(request):

    content = {
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/index.html', content)


def catalog_list(request):

    query = get_list_or_404(models.Product)
    query_category = get_list_or_404(models.Category)

    content = {
        'res_cat': query_category,
        'results': query,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/catalog.html', content)


def product_detail(request, pk):

    obj = get_object_or_404(models.Product, id=pk)

    content = {
        'instance': obj,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/brooch.html', content)


def contacts(request):

    content = {
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/contacts.html', content)
