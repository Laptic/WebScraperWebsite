import django_filters
from .models import RamParts,GpuParts,MotherboardParts

class RamFilter(django_filters.FilterSet):

    class Meta:
        model = RamParts
        fields = {
            'name': ['icontains'],
            'price': ['gt','lt'],
        }


class GpuFilter(django_filters.FilterSet):

    class Meta:
        model = GpuParts
        fields = {
            'name': ['icontains'],
            'price': ['gt','lt'],
        }

class MotherboardFilter(django_filters.FilterSet):

    class Meta:
        model = MotherboardParts
        fields = {
            'name': ['icontains'],
        }
