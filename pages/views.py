from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,bedroom_choices,prices_choices
# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'prices_choices':prices_choices
    }
    return render(request,"pages/index.html",context)

def about(request):
    realtors=Realtor.objects.all()
    mvp=Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp':mvp
    }
    return render(request,"pages/about.html",context)