from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices 
from contacts.models import reviews

# api

from .serializer import listingserializer
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    comments = reviews.objects.filter(post=listing_id)
    context = {
        'listing': listing,
        'comments':comments
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # KEYWORDS
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # STATE
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # BEDROOMS
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


# ----------------------------------------------------------------------------------------

# api of all listing and get listing by id

class listingAPIView(APIView):
    
        # READ a employee
        def get_object(self, pk):
            try:
                return Listing.objects.get(pk=pk)
            except Listing.DoesNotExist:
                raise Http404
        # get the employee by id otherwise all the employee
        def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = listingserializer(data)
                return Response(serializer.data)

            else:
                data = Listing.objects.all()
                serializer = listingserializer(data, many=True)

                return Response(serializer.data)
      
        # delete the employee
        def delete(self, request, pk, format=None):
            emp_to_delete =  listing.objects.get(pk=pk)

            # delete the todo
            emp_to_delete.delete()

            return Response({
                'message': 'listing Deleted Successfully'
            })