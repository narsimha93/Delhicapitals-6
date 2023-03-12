from django.shortcuts import render, redirect
from .models import Bookings
from django.contrib import messages
# Create your views here.



def booking (request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        adhar_card = request.POST['adhar_card']
        pan_card  = request.POST['pan_card']
        family_members = request.POST['family_members']
        aggrement = request.POST['aggrement']
        realtor_email = request.POST['realtor_email']
        user_id = request.user

        # Check if user has made transportation already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Bookings.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already book the house request')
                return redirect('/listings/'+listing_id)

        contact = Bookings( listing_id_id=int(listing_id), name=name, email=email, phone_number=phone_number,
                           adhar_card=adhar_card, pan_card=pan_card,family_members=family_members ,
                           aggrement=aggrement,user_id_id=user_id )

        contact.save()

        # SEND EMAIL
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry fro ' + listing + '. Sign in to the admin panel for more information.',
        #     'realestate@gmail.com',
        #     [realtor_email, ],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
       
        return redirect('/listings/'+listing_id)
   # return render(request,"booking/bookings.html")
    

def allbookings(request):
    booking = Bookings.objects.filter(user_id=request.user)
    #context = {'allbook':allbook}
    print(booking)
    return render(request, "booking/bookings.html", {'booking':booking})