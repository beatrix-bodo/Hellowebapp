from django.contrib import admin

from collection.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Quote, QuoteAdmin)
