import django_tables2 as tables
from .models import Deals

class DealsTable(tables.Table):
    class Meta:
        model = Deals
        template_name = 'accounts1.html'