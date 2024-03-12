from faker import Faker
import random
from api.models import Item

fake = Faker()

# Define custom categories
categories = ["Electronics", "Vegetables", "Food", "Clothing", "Books"]

subcategories = {
    "Books": ["Fiction", "Non-Fiction"],
    "Clothing": ["Men's", "Women's"],
    "Food": ["Fruits", "Vegetables", "Snacks"],
    "Vegetables": ["Green Vegetables", "Root Vegetables"],
    "Electronics": ["Phones", "Laptops", "Accessories"],
}

# Specific names based on categories
names_by_category = {
    "Books": [
        "Mahatma Gandhi – The Story Of My Experiments With The Truth",
        "R.K. Narayan – The Guide",
        "Rohinton Mistry – A Fine Balance",
        # ... (add other names)
    ],
    "Clothing": [
        "Nike",
        "Louis Vuitton",
        "Chanel",
        # ... (add other names)
    ],
    "Food": [
        "Aloo gobi",
        "Aloo tikki",
        "Bhindi masala",
        # ... (add other names)
    ],
    "Vegetables": [
        "Baingan",
        "Karela",
        "Patta gobhi",
        # ... (add other names)
    ],
    "Electronics": [
        "Apple",
        "Samsung",
        "Google Pixel",
        # ... (add other names)
    ],
}

# Use the custom category list with the random provider
fake.add_provider(random)

for _ in range(100):
    category = fake.random_element(categories)
    subcategory = fake.random_element(subcategories[category])
    name = fake.random_element(names_by_category[category])
    amount = random.randint(1, 100)

    item_data = {
        "category": category,
        "subcategory": subcategory,
        "name": f"{category} - {name}",  # Combine category with name
        "amount": amount,
    }
    Item.objects.create(**item_data)

# exec(open('/home/ubox48/PycharmProjects/django_orm/django_orm/api/test.py').read())
