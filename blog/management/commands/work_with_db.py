from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories_list = []
        # Здесь мы получаем данные из фикстур с категориями
        with open("blogs.json", mode="r", encoding="utf-8") as f:
            for item in json.load(f):
                if item["model"] == "blogs.category":
                    new_cat = {
                        "name": item["fields"]["name"],
                        "description": item["fields"]["description"],
                    }
                    categories_list.append(new_cat)
            print(categories_list)
            return categories_list

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстур с продуктами
        prod_list = []
        with open("blogs.json", mode="r", encoding="utf-8") as f:
            for item in json.load(f):
                if item["model"] == "blogs.product":
                    new_prod = {
                        "name": item["fields"]["name"],
                        "description": item["fields"]["description"],
                        "preview": item["fields"]["preview"],
                        "category": item["fields"]["category"],
                        "price": item["fields"]["price"],
                        "created_at": item["fields"]["created_at"],
                        "updated_at": item["fields"]["updated_at"],
                    }
                    prod_list.append(new_prod)
            print(prod_list)
            return prod_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category["name"], description=category["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    preview=product["preview"],
                    # получаем категорию из базы данных для корректной связки объектов
                    category=product["category"],
                    price=product["price"],
                    created_at=product["created_at"],
                    updated_at=product["updated_at"],
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
