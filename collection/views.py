from django.shortcuts import render
from collection.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', {
        'quotes': quotes,
    })
