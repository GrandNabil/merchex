
# ~/projects/django-web-app/merchex/listings/views.py
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Song
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id = id) #la ligne permet d'obtenir le Band avec l'ID
    #return render(request,'listings/band_detail.html', {'id': id})  #création de la vue détaillée, en ajoutant l'id au modèle
    return render(request,'listings/band_detail.html', {'band': band}) #mise à jour de la vue pour passer le groupe au gabarit

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()
    return render(request, 'listings/band_create.html',{'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)#on récupère le model qui a pour ID celui passé en paramètre
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  ## on récupère l'objet et on le passe au modèle
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
    return render(request, 'listings/band_delete.html', {'band': band})



def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

'''def listings_list(request):
    songls = Song.objects.all()
    return render(request, 'listings/listings_list.html', {'songs': songs})'''

def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings_list.html', {'listings': listings})

def listings_detail(request, id):
    listing = Listing.objects.get(id=id)#on récupère l'annonce à partir de son ID
    return render(request, 'listings/listings_detail.html', {'listing': listing})
def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            #créer un nouveau annonce et enregistrer dans la base de données
            listings = form.save()
            #rediriger vers la page de détails des annonces qui vient d’être créée
            return redirect ('listings-detail', listings.id)
    else :
        form = ListingForm()
        
    return render (request,'listings/listings_create.html', {'form':form})

def listings_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/band_update.html', {'form': form})
    
def listings_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings-list')
    return render(request, 'listings/listings_delete.html', {'listing':listing})


def contact(request):
    # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        
        return redirect('email-sent') # instruction de retour après une requete POST pour éviter un double POST
    

    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form}) #passe ce formulaire au gabarit