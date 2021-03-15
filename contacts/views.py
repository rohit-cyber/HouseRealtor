from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
                user_id=request.user.id
                has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
                if has_contacted:
                        messages.error(request,'Yor enquiry is already saved')
                        return redirect('/listings/'+listing_id)
        
        #Send_MAil
        send_mail('A new Enquiry from a customer',
                   "i have enquired for this " +listing +"\n" +message,
                   'rohitjune1994@gmail.com',
                   [realtor_email,'rohitjune06@gmail.com','rohitjune15@gmail.com','vivekravat15@gmail.com','amitabpradhan888@gmail.com'],
                   fail_silently=False)
         
        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        messages.success(request,"Your request have been saved, the retailor will soon contact you")
        return redirect('/listings/'+listing_id)
 