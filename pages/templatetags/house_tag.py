from listings.models import Listing
from django import template

register=template.Library()

@register.simple_tag
def total_listings():
    return Listing.objects.count()

@register.inclusion_tag('pages/index2.html')
def show_latest_house():
    latest_listings=Listing.objects.order_by('-list_date')[:100]
    return{'latest_listings':latest_listings}
