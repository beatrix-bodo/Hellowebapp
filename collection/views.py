from django.shortcuts import render
from collection.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', {
        'quotes': quotes,
    })

def quote_detail(request, slug):
    quote = Quote.objects.get(slug=slug)
    return render(request, 'quotes/quote_detail.html', {
        'quote': quote,
    })
