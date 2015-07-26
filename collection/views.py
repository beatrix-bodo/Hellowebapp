from django.shortcuts import render, redirect
from collection.forms import QuoteForm
from collection.models import Quote

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

def edit_quote(request, slug):
    quote = Quote.objects.get(slug=slug)
    form_class = QuoteForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_detail', slug=quote.slug)
    else:
        form = form_class(instance=quote)
    return render(request, 'quotes/edit_quote.html', {
        'quote': quote,
        'form': form,
    })
