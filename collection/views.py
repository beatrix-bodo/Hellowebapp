from django.shortcuts import render

# Create your views here.
def index(request):
    number = 6
    quote = "Quote title"
    return render(request, 'index.html', {
        'number': number,
        'quote': quote,
    })
