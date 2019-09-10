from banks.models import *
from django.contrib.auth.models import User
import django_filters


class DealsFilter(django_filters.FilterSet):
    #deal_number = django_filters.CharFilter(lookup_expr='icontains')
    #deal_number__gte = django_filters.NumberFilter(lookup_expr='number__gte')
    #deal_number__lte = django_filters.NumberFilter(lookup_expr='number__lte')
    #deal_number__gt = django_filters.NumberFilter(field_name = "zzzzz" lookup_expr='gt')
    #deal_number__gt = django_filters.NumberFilter(field_name='deal_number', lookup_expr='number__gt')

    CHOICES = (
            ("ascending", "Ascending"),
            ("descending", "Descending")
    )

    ordering = django_filters.ChoiceFilter(label = "Ordering by deal no", choices = CHOICES, method = "filter_by_order", empty_label="(Nothing)")
    frontoffice = django_filters.ModelChoiceFilter(queryset = User.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = Deals
#        fields = ["deal_number", "deal_date", "value_date", "deal_kind", "counterparty"]
        fields = {"deal_number": ["contains", "gte", "lte"], "counterparty": ["exact"], "deal_date": ["gte", "lte"], "value_date": ["gte", "lte"], "deal_kind": ["exact"], "frontoffice":["exact"]}

    def filter_by_order (self, queryset, name, value):
        expression = 'deal_number' if value == 'ascending' else '-deal_number'
        return queryset.order_by(expression)
