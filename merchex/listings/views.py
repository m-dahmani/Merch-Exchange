# from django.http import HttpResponse
# from listings.models import Band
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, Listing
from .forms import ContactUsForm, BandForm, ListingForm


# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})


def band_detail(request, band_id):
    # to recover the band(obj) and handle the case where the object does not exist.
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        raise Http404("No Band matches the given query.")
    
    # context = {'id': band_id} we pass the id to the model
    context = {'band': band}  # to pass the band to the template
    return render(request, 'listings/band_detail.html', context)


def listing_list(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings/listing_list.html', context)


def listing_detail(request, listing_id):
    # to recover the listing(obj) and handle the case where the object does not exist.
    listing = get_object_or_404(Listing, id=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing_detail.html', context)


def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # Create an instance of our form and fill it with the POST data
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            # Redirect to confirmation page
            return redirect('email-sent')  # We can redirect the browser from the original page to a new page
        
    # if the form is invalid, we let execution continue until return
    # below and display the form again (with errors).
    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()    # Add a new form here
        
    context = {'form': form}  # pass this form to the template
    return render(request, 'listings/contact.html', context)


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def band_create(request):
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        # Create an instance of our form and fill it with the POST data
        form = BandForm(request.POST)
        
        if form.is_valid():
            # create a new “Band” and save it in the database
            band = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the arguments of the url pattern as arguments to the redirect function
            return redirect('band-detail', band.id)
        
    # if the form is invalid, we let execution continue until return
    # below and display the form again (with errors).
    else:
        # this must be a GET request, so create an empty form
        form = BandForm()  # Add a new BandForm empty here if request.GET
    
    context = {'form': form}  # pass this form to the template
    return render(request, 'listings/band_create.html', context)


def listing_create(request):
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        # Create an instance of our form and fill it with the POST data
        form = ListingForm(request.POST)
        
        if form.is_valid():
            # create a new “Listing” and save it in the database
            listing = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the arguments of the url pattern as arguments to the redirect function
            return redirect('listing-detail', listing.id)
    
    # if the form is invalid, we let execution continue until return
    # below and display the form again (with errors).
    else:
        # this must be a GET request, so create an empty form
        form = ListingForm()  # Add a new ListingForm empty here if request.GET
    
    context = {'form': form}  # pass this form to the template
    return render(request, 'listings/listing_create.html', context)


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        # we pre-fill the form with an existing band the instance already created and fill it with the POST data
        form = BandForm(request.POST, instance=band)
        
        if form.is_valid():
            # update the instance of the object already created “Band” and save it in the database
            band = form.save()
            # redirect to the detail page of the band we just update
            # we can provide the arguments of the url pattern as arguments to the redirect function
            return redirect('band-detail', band.id)
    
    # if the form is invalid, we let execution continue until return
    # below and display the form again (with errors).
    else:
        # we pre-fill the form with an existing band the instance already created
        # this must be a GET request, so open with the instance of the object already created
        form = BandForm(instance=band)  # we pre-fill the form with an existing band here if request.GET
    
    context = {'form': form}  # pass this form to the template
    return render(request, 'listings/band_update.html', context)


def listing_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        # we pre-fill the form with an existing listing the instance already created and fill it with the POST data
        form = ListingForm(request.POST, instance=listing)
        
        if form.is_valid():
            # update the instance of the object already created “Listing” and save it in the database
            listing = form.save()
            # redirect to the detail page of the listing we just update
            # we can provide the arguments of the url pattern as arguments to the redirect function
            return redirect('listing-detail', listing.id)
    
    # if the form is invalid, we let execution continue until return
    # below and display the form again (with errors).
    else:
        # we pre-fill the form with an existing listing the instance already created
        # this must be a GET request, so open with the instance of the object already created
        form = ListingForm(instance=listing)  # we pre-fill the form with an existing listing here if request.GET
    
    context = {'form': form}  # pass this form to the template
    return render(request, 'listings/listing_update.html', context)


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # delete the band object in the database
            band.delete()
            # redirect to the list-page of the band we just verified if existing it
            return redirect('band-list')
        
        elif 'cancel' in request.POST:
            # redirect to the list-page without delete
            return redirect('band-list')
        
    # no need for “else” here. If it's a GET request, just continue
    
    context = {'band': band}  # to pass the band to the template
    return render(request, 'listings/band_delete.html', context)


def listing_delete(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    # Take a look at « request.method » and « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # delete the listing object in the database
            listing.delete()
            # redirect to the list-page of the listing we just verified if existing it
            return redirect('listing-list')
        
        elif 'cancel' in request.POST:
            # redirect to the list-page without delete
            return redirect('listing-list')
    
    # no need for “else” here. If it's a GET request, just continue
    
    context = {'listing': listing}  # to pass the band to the template
    return render(request, 'listings/band_delete.html', context)















# def manage_band_listings(request, band_id, listing_id):
#     # to recover the band(obj) and handle the case where the object does not exist.
#     band = get_object_or_404(Band, id=band_id) # or band = Band.objects.get(id=band_id)
#     listing = get_object_or_404(Listing, id=listing_id)
#     listings = band.listing_set.all()
#     if request.method == 'GET':
#         if listing.band:
#             band = get_object_or_404(Band, id=band_id)
#             listings.band = BandForm(instance=band)
#             return redirect('manage-band-listings')
#
#     context = {'band': band, 'listings': listings}
#     return render(request, 'listings/manage_band_listings.html', context)
