from django.contrib import admin

from listings.models import Band    #Enregistrer Band le modèle sur le site d'administration de django.
from listings.models import Listing #Enregistrer le modèle Listings sur le site d'administration de django

#afficher le genre et l'année de formation du groupe sur cette liste
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') #les champs que nous voulons afficher

class ListingAdmin(admin.ModelAdmin):
   # list_display = ('description', 'year')
    list_display = ('title', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
