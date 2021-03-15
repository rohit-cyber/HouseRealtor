from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    model=Listing
    list_display=['id','title','city','state','is_published','realtor','list_date']
    search_fields=('city','state','description','realtor__name')
    list_filter=('state',)
    list_display_links=('id','title')
    list_editable=('is_published',)
admin.site.register(Listing,ListingAdmin)

