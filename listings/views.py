from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from .choices import state_choices,bedroom_choices,prices_choices

# Create your views here.
def index(request):
    listings=Listing.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings,3) # Show 3 contacts per page
    page = request.GET.get('page')
    listing_page= paginator.get_page(page)

    context={'listings':listing_page}
    return render(request,"listings/listings.html",context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request,"listings/listing.html",context)

def search(request):
    query_list=Listing.objects.order_by('-list_date').filter(is_published=True)

    #keywords
    if 'keywords' in request.GET:
        keyword=request.GET['keywords']
        if keyword:
            query_list=Listing.objects.filter(description__icontains=keyword)
    
    #city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_list=Listing.objects.filter(city__iexact=city)
    
    #state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            query_list=Listing.objects.filter(state__iexact=state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            query_list=Listing.objects.filter(bedroom__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_list=Listing.objects.filter(price__lte=price)

    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'prices_choices':prices_choices,
        'listings':query_list,
        'values':request.GET
    }
    return render(request,"listings/search.html",context)