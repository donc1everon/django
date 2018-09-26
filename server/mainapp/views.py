from django.shortcuts import render

goods = [
    {'href': 'brooch', 'img': 'cheshire_cat.jpg', 'name': 'Брошь Чеширский кот'},
    {'href': 'brooch', 'img': 'http://placehold.it/100x82', 'name': 'Товар 2'},
    {'href': 'brooch', 'img': 'http://placehold.it/100x82', 'name': 'Товар 3'},
    {'href': 'brooch', 'img': 'http://placehold.it/100x82', 'name': 'Товар 4'},
    {'href': 'brooch', 'img': 'http://placehold.it/100x82', 'name': 'Товар 5'},
]
links_menu = [
    {'href': 'main_page', 'name': 'главная'},
    {'href': 'catalog', 'name': 'каталог'},
    {'href': 'contacts', 'name': 'контакты'},
]


def catalog_list(request):

    content = {
        'goods': goods,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/catalog.html', content)


def main_page(request):

    content = {
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/index.html', content)


def product_detail(request):

    content = {
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/brooch.html', content)


def contacts(request):

    content = {
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/contacts.html', content)
