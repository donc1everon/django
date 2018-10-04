from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from authapp.models import ShopUser


import json, os

JSON_PATH = 'mainapp/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = loadFromJSON('categories')

        Category.objects.all().delete()

        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()

        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = Category.objects.get(title=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # super_user = ShopUser.objects.create_superuser('ad_test', 'django@geekshop.local', 'geekbrains', age=28)
