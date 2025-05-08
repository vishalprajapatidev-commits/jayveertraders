from django.shortcuts import render
from .models import Product, ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
from django.shortcuts import render, redirect
import traceback  
import sys  



def home(request):
    featured_products = Product.objects.filter(featured=True)[:6]
    return render(request, 'home.html', {'featured_products': featured_products})

def about(request):
    return render(request, 'about.html')


def products(request):
    tiles = Product.objects.filter(product_type='TILE')
    granite = Product.objects.filter(product_type='GRANITE')
    marble = Product.objects.filter(product_type='MARBLE')
    return render(request, 'products.html', {
        'tiles': tiles,
        'granite': granite,
        'marble': marble
    })



def contact_view(request):
    if request.method == 'POST':
        try:
            # Your existing form processing code
            contact = ContactMessage(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
            contact.save()
            
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
            
        except Exception as e:
            # Print full error to console
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("\n" + "="*50)
            print("FULL ERROR DETAILS:")
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stdout)
            print("="*50 + "\n")
            
            messages.error(request, 'We encountered an error. Please try again.')
            
    return render(request, 'contact.html')

def location_view(request):
    return render(request, 'locations.html')  # Note the plural 'locations.html'

def home(request):
    return render(request, 'home.html')