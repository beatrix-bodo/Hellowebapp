from django.forms import ModelForm
from collection.models import Quote

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ('name', 'description')
