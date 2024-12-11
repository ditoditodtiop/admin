from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag

class Command(BaseCommand):
    help = "Call custom manager methods and process their results."

    def handle(self, *args, **kwargs):
        categories = Category.objects.with_item_count()

        for category in categories:
            print(f"Category: {category.name}, Item Count: {category.item_count}")

        items = Item.objects.with_tag_count()

        for item in items:
            print(f"Item: {item.name}, Tags Count: {item.tags_count}")

        min_items = 5
        popular_tags = Tag.objects.popular_tags(min_items=min_items)

        for tag in popular_tags:
            print(f"Tag: {tag.name}, Item Count: {tag.item_count}")