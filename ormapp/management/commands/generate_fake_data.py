from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Item
import random


class Command(BaseCommand):
    help = 'Generate fake data for the Item model'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating fake data...'))

        fake = Faker()

        categories = ["Electronics", "Vegetables", "Food", "Clothing", "Books"]

        subcategories = {
            "Books": ["Fiction", "Non-Fiction"],
            "Clothing": ["Men's", "Women's"],
            "Food": ["Fruits", "Vegetables", "Snacks"],
            "Vegetables": ["Green Vegetables", "Root Vegetables"],
            "Electronics": ["Phones", "Laptops", "Accessories"],
        }

        names_by_category = {
            "Books": ["Mahatma Gandhi – The Story Of My Experiments With The Truth",
                      "R.K. Narayan – The Guide",
                      "Rohinton Mistry – A Fine Balance",
                      "Salman Rushdie – Midnight’s Children",
                      "Jhumpa Lahiri – The Interpreter Of Maladies",
                      "Vikram Seth – A Suitable Boy",
                      "Arundhati Roy – God of Small Things",
                      "Amitav Ghosh – The Glass Palace",
                      "Kiran Desai – The Inheritance of Loss",
                      "Mulk Raj Anand – The Private Life of an Indian Prince",
                      "Vikram Chandra – Red Earth and Pouring Rain",
                      "Suketu Mehta – Maximum City",
                      "Rabindranath Tagore – Gitanjali",
                      "Mitra Phukan – The Collector’s Wife",
                      "Khushwant Singh – Train to Pakistan",
                      "Nayantara Sehgal – Rich Like Us",
                      "Anita Desai – In Custody",
                      "Sunetra Gupta – The Glassblower’s Breath",
                      "A. K. Ramanujan – The Collected Poems",
                      "Nirad C. Chaudhuri, The Autobiography of an Unknown Indian"],  # Add your book names here
            "Clothing": ["Nike",
                         "Louis Vuitton",
                         "Chanel",
                         "Gucci",
                         "Adidas",
                         "Hermès",
                         "Dior",
                         "Cartier",
                         "Zara",
                         "Rolex",
                         "H&M",
                         "UNIQLO",
                         "Tiffany & Co",
                         "Coach",
                         "Chow Tai Fook",
                         "Lululemon",
                         "Burberry",
                         "Prada",
                         "Puma",
                         "Omega"],  # Add your clothing names here
            "Food": ["Aloo gobi",
                     "Aloo tikki",
                     "Bhindi masala",
                     "Bhatura",
                     "Biryani",
                     "Chaat",
                     "Chapati",
                     "Daal baati churma",
                     "Poha",
                     "Gobhi matar",
                     "Jalebi",
                     "Kadai paneer",
                     "Khichdi",
                     "Kulfi falooda",
                     "Litti chokha",
                     "Missi roti",
                     "Mixed vegetable",
                     "Palak paneer",
                     "Pani puri",
                     "Paratha"],  # Add your food names here
            "Vegetables": ["Baingan",
                           "Karela",
                           "Patta gobhi",
                           "Gajar",
                           "Shimla mirch",
                           "Phool gobi",
                           "Nariyal",
                           "Makai, bhutta",
                           "Kheera",
                           "Methi",
                           "Adrak",
                           "Hari mirch",
                           "Nimbu",
                           "Pyaaz",
                           "Bhindi",
                           "Matar",
                           "pudina",
                           "Kaddu",
                           "Aloo",
                           "Tamatar"],  # Add your vegetable names here
            "Electronics": ["Apple",
                            "Samsung",
                            "Google Pixel",
                            "Xiaomi",
                            "Huawei",
                            "OnePlus",
                            "Oppo",
                            "Vivo",
                            "Sony",
                            "Realme",
                            "Motorola",
                            "Asus",
                            "Tecno Mobile",
                            "LG",
                            "ZTE",
                            "Nokia",
                            "HTC",
                            "Panasonic",
                            "Honor",
                            "Alcatel-Lucent"],  # Add your electronics names here
        }

        for _ in range(100):
            category = fake.random_element(categories)
            subcategory = fake.random_element(subcategories[category])
            name = fake.random_element(names_by_category[category])
            amount = random.randint(1, 100)

            item_data = {
                "category": category,
                "subcategory": subcategory,
                "name": name,
                "amount": amount,
            }
            Item.objects.create(**item_data)

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully.'))
