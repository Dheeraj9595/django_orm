from rest_framework import serializers
from ormapp.models import Employee

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         # fields = '__all__'
#         # exclude = (created_by)
#         fields = ['id','name', 'age','experience_in_years', 'state']


from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# class PaginatedEmployeeSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         # Wrap the serialized data in a dictionary with the 'results' key
#         return {'results': super(PaginatedEmployeeSerializer, self).to_representation(data)}

class PaginatedEmployeeSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # Call the parent class method without wrapping in an additional dictionary
        return super(PaginatedEmployeeSerializer, self).to_representation(data)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        list_serializer_class = PaginatedEmployeeSerializer  # Use the custom ListSerializer for pagination
