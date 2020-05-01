import django_filters
from .models import Cat

class CatlistFilter(django_filters.FilterSet):
    
    class Meta:
        model = Cat
        fields = ('location','gender','breed','entrydate')
