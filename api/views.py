from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from api.serializers import ItemSerializer
from rest_framework import serializers, status
from faker import Faker
from api.models import Item  # Import your Item model


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    # validation for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


fake = Faker()


def fake_data():
    # Generate random data and create an Item object
    random_item_data = {
        "category": fake.word(),
        "subcategory": fake.word(),
        "name": fake.word(),
        "amount": fake.random_int(min=1, max=100),
    }

    item = Item.objects.create(**random_item_data)
    print(f"Created Item: {item}")
